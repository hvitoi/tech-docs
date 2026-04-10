import asyncio

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


async def index_documents_async(documents: list[Document], batch_size: int = 50):
    """Process documents in batches asynchronously."""
    print("=== VECTOR STORAGE PHASE ===")
    print(f"Preparing to add {len(documents)} documents to vector store")

    batches = [
        documents[i : i + batch_size] for i in range(0, len(documents), batch_size)
    ]
    print(f"Split into {len(batches)} batches of {batch_size} documents each")

    async def add_batch(batch: list[Document], batch_num: int):
        try:
            await vector_store.aadd_documents(batch)
            print(f"  Added batch {batch_num}/{len(batches)} ({len(batch)} documents)")
        except Exception as e:
            print(f"  Failed batch {batch_num} - {e}")
            return False
        return True

    tasks = [add_batch(batch, i + 1) for i, batch in enumerate(batches)]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    successful = sum(1 for result in results if result is True)
    print(f"Indexed {successful}/{len(batches)} batches successfully")


async def main():
    print("=== DOCUMENTATION INGESTION PIPELINE ===")

    print("Crawling documentation site...")
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
    print(f"Splitting {len(docs)} documents (chunk_size=4000, overlap=200)...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=200)
    split_docs: list[Document] = text_splitter.split_documents(docs)
    print(f"Created {len(split_docs)} chunks from {len(docs)} documents")

    # Process documents asynchronously
    await index_documents_async(split_docs, batch_size=500)

    print("=== PIPELINE COMPLETE ===")
    print(f"  Documents extracted: {len(docs)}")
    print(f"  Chunks created: {len(split_docs)}")


if __name__ == "__main__":
    asyncio.run(main())
