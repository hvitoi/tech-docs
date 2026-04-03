# RAG (Retrieval-augmented generation)

- <https://en.wikipedia.org/wiki/Retrieval-augmented_generation>
- Attempts to solve the problem about making the LLM know about information on which it was not trained on

```shell
pip install -U langgraph "langchain[openai]" langchain-community langchain-text-splitters bs4
```

```shell
export PINECONE_API_KEY=pcsk_...
export
```

## Document loaders

- <https://docs.langchain.com/oss/python/integrations/document_loaders>
- Document loaders provide a standard interface for reading data from different sources (such as Slack, Notion, or Google Drive) into LangChain's Document format.

- Types
  - `WebBaseLoader`: loads an website <https://docs.langchain.com/oss/python/integrations/document_loaders/web_base>

## Text splitter

- <https://docs.langchain.com/oss/python/integrations/splitters>
- Text splitters break large docs into smaller chunks that will be retrievable individually and fit within model context window limit.

## Vector DB

- <https://docs.langchain.com/oss/python/integrations/providers/pinecone>
