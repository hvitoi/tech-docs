# Langchain

- <https://docs.langchain.com/oss/python/langchain/overview>
- LangChain is an open source framework with an agent architecture and integrations with several LLMs
- Build LLM-powered applications
- It abstracts the process of interacting with the LLM
- Supports agent ecosystem (e.g., search on internet, query database, send emails)

## Documentation

- Reference <https://reference.langchain.com/python/langchain/>
- Docs <https://docs.langchain.com/oss/python/langchain/overview>

## Models

- The models (LLMs from an AI provider) can be utilized in 2 ways
  1. With agents
  2. Standalone: called outside of the agent loop for tasks like text generation, classification, etc

- The models can be initialized using:
  1. Using langchain.chat_models.init_chat_model
  1. Using provider-specific classes langchain_google_genai.ChatGoogleGenerativeAI, langchain_openai.ChatOpenAI, etc

```shell
pip install langchain[openai]
pip install langchain[google-genai]
pip install langchain[ollama]

uv add langchain-openai
uv add langchain-google-genai
uv add langchain-ollama
```

## LangChain Expression Language (LCEL)

- It's new syntax introduced to simplify the creation of chains in LangChain applications

```python
chain: Runnable = prompt_template | model
chain: Runnable = prompt_template.__or__(model) # same
```
