# History Shortening

## Stuffing

## Summarization

- Compress history into shorter form
- <https://docs.langchain.com/oss/python/langchain/middleware/built-in#summarization>
  - `Stuffing`: no summarization at all, just stuff the whole document into the prompt
  - `Map Reduce`: send parallel requests to LLM to summarize each document/part and then integrate it all in a smaller prompt
  - `Refine`: basically a reduce operation. pass "acc + el" to the LLM to summarize

## Truncation

- Trim old messages
- dropping old tokens/messages, simplest strategy
