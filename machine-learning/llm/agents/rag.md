# RAG (Retrieval-Augmented Generation)

- RAG allows the LLM to `retrieve relevant information` from external sources rather than using only what it learned during training
- Then this information is used to `augment the prompt`
- Useful to reason about private documents or information, because the model was not trained with it
- <https://en.wikipedia.org/wiki/Retrieval-augmented_generation>

## Why not just "stuff" the whole information into the prompt?

- Example: you want to ask a question about a book, then just attach the whole book into the prompt
- That doesn't scale!
  - Hard token limit
  - `Needle in the Haystack` - Context Rot (LLMs tend to become less effective with long prompts) <https://arxiv.org/abs/2407.01437>
  - Cost
  - Latency
- Therefore we need another way to embed this information into the prompt

## RAG Implementation

1. Take the entire document
2. Split it into smaller chunks (text splitters)
3. Transform each of those chunks into embeddings and save it into a vector database
4. Search through the embeddings with the original prompt in order to know which are the most relevant chunks

![RAG Pipeline](.images/rag-pipeline.png)

## Fine-tuning as an alternative

Some argue that fine-tuning on domain knowledge is more reliable than retrieval - no retrieval errors, no chunking artifacts, no context stuffing issues.

## RAG types

- `Graph RAG`: combines knowledge graphs with vector search
- `Agentic RAG`: multi-step retrieval with planning
- `HyDE`, `FLARE`, `RAPTOR`: smarter retrieval strategies
- `Rerankers`: cross-encoder models improve precision

| Architecture  | Description                                                               | Control    | Flexibility | Latency       | Example Use Case                                    |
|---------------|---------------------------------------------------------------------------|------------|-------------|---------------|-----------------------------------------------------|
| 2-Step RAG    | Retrieval always happens before generation. Simple and predictable.       | ✅ High    | ❌ Low      | ⚡ Fast       | FAQs, documentation bots                            |
| Agentic RAG   | An LLM-powered agent decides when and how to retrieve during reasoning.   | ❌ Low     | ✅ High     | ⏳ Variable   | Research assistants with access to multiple tools   |
| Hybrid        | Combines characteristics of both approaches with validation steps.        | ⚖️ Medium  | ⚖️ Medium   | ⏳ Variable   | Domain-specific Q&A with quality validation         |
