from bs4 import BeautifulSoup
from langchain.agents import create_agent
from langchain.embeddings import init_embeddings
from langchain.tools import tool
from langchain_community.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

# The LLM decides when to retrieve the documentation from vectorstore (through function calling)

embedding_model = init_embeddings("openai:text-embedding-3-small")
vector_store = InMemoryVectorStore(embedding_model)


def bs4_extractor(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n", strip=True)


def ingest():
    print("=== Crawling website ===")
    loader = RecursiveUrlLoader(
        url="https://python.langchain.com/",
        max_depth=2,
        extractor=bs4_extractor,
    )
    docs: list[Document] = loader.load()
    print(f"Crawled {len(docs)} pages")

    print("=== Splitting documents ===")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=200)
    split_docs: list[Document] = text_splitter.split_documents(docs)
    print(f"Created {len(split_docs)} chunks from {len(docs)} documents")

    print("=== Indexing to vector store ===")
    vector_store.add_documents(split_docs)
    print(f"Indexed {len(split_docs)} documents successfully")


# content_and_artifact: tells to the llm that:
# - ToolMessage.content: the 1st return value is the content (serialized) - the content is the actual tool result - the LLM will only receive this
# - ToolMessage.artifact: the 2nd is the artifact (retrieved_docs) - the artifact is the source, the original doc - the LLM never receives this
@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve relevant documentation to help answer user queries."""
    retrieved_docs = vector_store.as_retriever(search_kwargs={"k": 4}).invoke(query)

    serialized = "\n\n".join(
        f"Source: {doc.metadata.get('source', 'Unknown')}\n\nContent: {doc.page_content}"
        for doc in retrieved_docs
    )

    return serialized, retrieved_docs


system_prompt = (
    "You are a helpful AI assistant that answers questions about LangChain documentation. "
    "You have access to a tool that retrieves relevant documentation. "
    "Use the tool to find relevant information before answering questions. "
    "Always cite the sources you use in your answers. "
    "If you cannot find the answer in the retrieved documentation, say so."
)

agent = create_agent(
    "openai:gpt-5.4",
    tools=[retrieve_context],
    system_prompt=system_prompt,
)


if __name__ == "__main__":
    ingest()

    response = agent.invoke(
        {"messages": [{"role": "user", "content": "what are deep agents?"}]}
    )

    for msg in response["messages"]:
        print(f"[{msg.__class__.__name__}]: {msg.content[:100]}")
        # the ToolMessage has also the "artifact" attribute (apart form the "content")
