# Embeddings

- It's a `vector` (or an "embedding") created out of a object/text that represents the position this object in a high-dimension space
- An `embedding model` is used to create the vector/embedding of an object
- The distance between points (the objects) in this high-dimension represent how similar they are to each other.
- "How similar it is" can be how similar are the `semantic meanings` of the objects
- Embeddings are specially useful for RAG and searching by meaning

![Embeddings](.images/embeddings.png)
![Embeddings](.images/embeddings-semantic-meaning.png)

## Embeddings Models (Encoders)

- `OpenAI`: text-embedding-3-small, text-embedding-ada-002 (old)
- `Google`: gemini-embedding-001,
- `Voyage AI`: voyage-3-large. Recommended by Anthropic
- `Nomic AI`: nomic-embed-text. Open-source, available in Ollama
