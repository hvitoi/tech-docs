from bs4 import BeautifulSoup
from langchain.chat_models import init_chat_model
from langchain.embeddings import init_embeddings
from langchain_community.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

llm = init_chat_model("openai:gpt-5.4")
embedding_model = init_embeddings("openai:text-embedding-3-small")
vector_store = InMemoryVectorStore(embedding_model)


def bs4_extractor(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n", strip=True)


def main():
    print("=== Crawling website ===")
    # RecursiveUrlLoader fetches raw HTML from each page. That HTML is full of tags, scripts, nav bars, footers, etc. - not useful for an LLM or embeddings.
    # The extractor parameter tells the loader how to convert raw HTML into plain text for each page.
    loader = RecursiveUrlLoader(
        url="https://python.langchain.com/",
        max_depth=2,
        extractor=bs4_extractor,
    )
    docs: list[Document] = loader.load()
    print(f"Crawled {len(docs)} pages")

    # Split documents into chunks
    print("=== Splitting documents ===")
    print(f"Splitting {len(docs)} documents")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=200)
    split_docs: list[Document] = text_splitter.split_documents(docs)
    print(f"Created {len(split_docs)} chunks from {len(docs)} documents")

    print("=== Indexing to vector store ===")
    print(f"Adding {len(split_docs)} documents to vector store...")
    vector_store.add_documents(split_docs)
    print(f"Indexed {len(split_docs)} documents successfully")


if __name__ == "__main__":
    main()
