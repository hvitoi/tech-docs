# RAG (Retrieval-Augmented Generation)

- RAG allows the LLM to `retrieve relevant information` from external sources rather than using only what it learned during training
- Then this information is used to `augment the prompt`
- Useful to reason about private documents or information, because the model was not trained with it

## Why not just "stuff" the whole information into the prompt?

- Example: you want to ask a question about a book, then just attach the whole book into the prompt
- That doesn't scale!
  - Hard token limit
  - Needle in the Haystack (LLMs tend to become less effective with long prompts)
  - Cost
  - Latency
- Therefore we need another way to embed this information into the prompt

## RAG Implementation
