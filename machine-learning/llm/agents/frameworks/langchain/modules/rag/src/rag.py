from langchain.chat_models import init_chat_model
from langchain.embeddings import Embeddings, init_embeddings
from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)
from langgraph.graph import MessagesState

## DOCUMENT LOADER

urls = [
    "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/",
    "https://lilianweng.github.io/posts/2024-07-07-hallucination/",
    "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/",
]

docs: list[Document] = []

for url in urls:
    # each url may contain several documents
    docs.extend(WebBaseLoader(url).load())
# docs[0].page_content.strip()[:1000]  # accessing it


## TEXT SPLITTER: Break documents into chunks

# The RecursiveCharacterTextSplitter attempts to keep larger units (e.g., paragraphs) intact.
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # 100 tokens in each chunk
    chunk_overlap=50,  # allow some tolerance on the chunk size so that context is not lost in the middle of a sentence or phrase
)

# Uses "tiktoken", the tokenizer by OpenAI to count tokens (pip install tiktoken)
# text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#     encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0
# )

doc_splits: list[Document] = text_splitter.split_documents(docs)


## VECTOR DATABASE & EMBEDDING MODEL
# Choose the embeddings model to generate the vectors for the chunks
# Index the document chunks into a in-memory vector database
# Pull the model first "ollama pull nomic-embed-text"
embedding_model: Embeddings = init_embeddings("ollama:nomic-embed-text")
vector_store = InMemoryVectorStore.from_documents(
    documents=doc_splits,
    embedding=embedding_model,
)


## RETRIEVER
# Create a retrieve and a tool to invoke it
retriever = vector_store.as_retriever()


@tool
def retrieve_blog_posts(query: str) -> str:
    """Search and return information about Lilian Weng blog posts."""
    selected_docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in selected_docs])


# retrieve_blog_posts.invoke({"query": "types of reward hacking"}) # test its


##
llm = init_chat_model("anthropic:claude-sonnet-4-6", temperature=0)


def generate_query_or_respond(state: MessagesState):
    response = llm.bind_tools([retrieve_blog_posts]).invoke(state["messages"])
    return {"messages": [response]}


# a question that requires semantic search
input: MessagesState = {
    "messages": [
        HumanMessage("What does Lilian Weng say about types of reward hacking?")
    ]
}
generate_query_or_respond(input)["messages"][-1].pretty_print()
