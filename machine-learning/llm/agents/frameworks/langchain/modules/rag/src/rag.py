from operator import itemgetter

from langchain.chat_models import init_chat_model
from langchain.embeddings import Embeddings, init_embeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore, VectorStoreRetriever
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)
from pinecone import Pinecone

## DOCUMENT LOADER

urls = [
    "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/",
    "https://lilianweng.github.io/posts/2024-07-07-hallucination/",
    "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/",
]

selected_doc_chunks: list[Document] = []

for url in urls:
    # each url may contain several documents
    loader = WebBaseLoader(url)
    selected_doc_chunks.extend(loader.load())  # load the file as a LangChain document
# docs[0].page_content.strip()[:1000]  # accessing it


## TEXT SPLITTER: Break documents into chunks

# RecursiveCharacterTextSplitter attempts to keep larger units (e.g., paragraphs) intact.
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # 100 characters in each chunk
    chunk_overlap=50,  # allow some tolerance on the chunk size so that context is not lost in the middle of a sentence or phrase
)

# Uses "tiktoken", the tokenizer by OpenAI to count tokens (pip install tiktoken)
# Uses tokens instead of characters
# text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
#     encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0
# )

docs_chunks: list[Document] = text_splitter.split_documents(selected_doc_chunks)
print(f"Number of chunks: {len(docs_chunks)}")


## VECTOR DATABASE & EMBEDDING MODEL
# Choose the embeddings model to generate the vectors for the chunks
# Index the document chunks into a in-memory vector database
# Pull the model first "ollama pull nomic-embed-text"
# This embedding model has a fixes output dimension of 768
embedding_model: Embeddings = init_embeddings("ollama:nomic-embed-text")

# With InMemory Vector Store
vector_store = InMemoryVectorStore.from_documents(
    documents=docs_chunks,
    embedding=embedding_model,
)

# With Pinecone Vector Store
# pc = Pinecone()
# index = pc.Index("cazzo-duro")
# index.delete(delete_all=True)  # clear the index before adding more documents
# vector_store = PineconeVectorStore.from_documents(  # uses the PINECORE_API_KEY under the hood
#     docs_chunks,  # add the chunks to the index
#     embedding_model,
#     index_name="cazzo-duro",  # The pre-created index must match the 768 dimension of the embedding model
# )

# Test the vector store
# sample = vector_store.similarity_search("reward hacking hallucination diffusion", k=3)
# for i, doc in enumerate(sample, 1):
#     source = doc.metadata.get("source", "unknown")
#     preview = doc.page_content.strip().replace("\n", " ")[:80]
#     print(f"[{i}] {source}\n    {preview}...")


## RETRIEVER
# Create a retrieve and a tool to invoke it
# The retriever is a LangChain interface to interact with various types of vector stores
# get the top 3
retriever: VectorStoreRetriever = vector_store.as_retriever(search_kwargs={"k": 3})


def format_docs(docs):
    """Format retrieved documents into a single string."""
    return "\n\n".join(doc.page_content for doc in docs)


# LLM Model
llm = init_chat_model("anthropic:claude-sonnet-4-6", temperature=0)


prompt_template = ChatPromptTemplate.from_template(
    (
        "Answer the question based only on the following context:"
        "{context}"
        "Question: {question}"
        "Provide a detailed answer:"
    )
)


# Query
query = "what is Pinecone in machine learning?"

# ========================================================================
# Option 0: Raw invocation without RAG
# ========================================================================
print("\n" + "=" * 70)
print("IMPLEMENTATION 0: Raw LLM Invocation (No RAG)")
print("=" * 70)
result = llm.invoke([HumanMessage(content=query)])
print(result.content)

# ========================================================================
# Option 1: Use implementation WITHOUT LCEL (Simple Function-Based Approach)
# ========================================================================
print("\n" + "=" * 70)
print("IMPLEMENTATION 1: Without LCEL")
print("=" * 70)
# Step 1: Retrieve relevant documents
selected_doc_chunks = retriever.invoke(query)  # top 3

# Step 2: Format documents into context string
context = format_docs(selected_doc_chunks)

# Step 3: Format the prompt with context and question
messages = prompt_template.format_messages(context=context, question=query)

# Step 4: Invoke LLM with the formatted messages
result = llm.invoke(messages)

# Step 5: Print the content
print(result.content)

# ========================================================================
# Option 2: Use implementation With LCEL (LangChain Expression Language)
# ========================================================================
print("\n" + "=" * 70)
print("IMPLEMENTATION 2: With LCEL")
print("=" * 70)

retrieval_chain = (
    RunnablePassthrough.assign(context=itemgetter("question") | retriever | format_docs)
    | prompt_template
    | llm
    | StrOutputParser()
)

result = retrieval_chain.invoke({"question": query})
print(result)
