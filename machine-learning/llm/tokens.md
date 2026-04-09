# Tokens

- 1 token ≈ 3/4 of an English word, 1,000 tokens ≈ 750 words

- `Input tokens`
  - Your prompt
  - System instructions
  - Conversation history
  - Tool results
  - File contents

- `Output tokens`
  - The model's response

## Billing

- You are billed for both input and output tokens

## Context Window (Input tokens)

- The number of tokens an LLM can consider as input when generating text (the "size" of your prompt)
- Large context windows require more memory and processing power
- These days (2026) it's common to have a `1 million` context window limit

![Context Window](.images/context-window.png)

- Limits
  - GPT 3.5 (Nov 2022): 4k tokens - alongside ChatGPT launch
  - GPT 5.0 (Aug 2025): 1M tokens
  - Opus/Sonnet 4.6 (Fev 2026): 1M tokens

## Summarization Strategies

- <https://docs.langchain.com/oss/python/langchain/middleware/built-in#summarization>

- `Stuffing`: no summarization at all, just stuff the whole document into the prompt
- `Map Reduce`: send parallel requests to LLM to summarize each document/part and then integrate it all in a smaller prompt
- `Refine`: basically a reduce operation. pass "acc + el" to the LLM to summarize
- `Trim old messages`
