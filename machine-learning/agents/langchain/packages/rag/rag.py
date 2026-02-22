import os

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import MessagesState

## Load documents
os.environ["USER_AGENT"] = "MyLangChainApp"

urls = [
    "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/",
    "https://lilianweng.github.io/posts/2024-07-07-hallucination/",
    "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/",
]

docs: list[Document] = []

for url in urls:
    docs.extend(WebBaseLoader(url).load())
# docs[0].page_content.strip()[:1000]  # accessing it


## Break documents into chunks
# Uses "tiktoken", the tokenizer by OpenAI to count tokens
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=100,  # 100 tokens in each chunk
    chunk_overlap=50,  # allow some tolerance on the chunk size so that context is not lost in the middle of a sentence or phrase
)
doc_splits: list[Document] = text_splitter.split_documents(docs)


## Index the document chunks into a in-memory vector database
vectorstore = InMemoryVectorStore.from_documents(
    documents=doc_splits,
    embedding=OpenAIEmbeddings(),
)


## Create a retrieve and a tool to invoke it
retriever = vectorstore.as_retriever()


@tool
def retrieve_blog_posts(query: str) -> str:
    """Search and return information about Lilian Weng blog posts."""
    docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in docs])


# retrieve_blog_posts.invoke({"query": "types of reward hacking"}) # test its


##
llm = init_chat_model("ollama:llama3.2", temperature=0)


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
