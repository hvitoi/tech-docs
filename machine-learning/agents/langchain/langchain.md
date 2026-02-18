# Langchain

- <https://docs.langchain.com/oss/python/langchain/overview>
- LangChain is an open source framework with an agent architecture and integrations with several LLMs
- Build LLM-powered applications
- It abstracts the process of interacting with the LLM
- Supports agent ecosystem (e.g., search on internet, query database, send emails)

## Documentation

- Reference <https://reference.langchain.com/python/langchain/>
- Docs <https://docs.langchain.com/oss/python/langchain/overview>

## LangChain Expression Language (LCEL)

- It's new syntax introduced to simplify the creation of chains in LangChain applications

```python
chain: Runnable = prompt_template | model
chain: Runnable = prompt_template.__or__(model) # same
```

## Evolution of Agents

1. `ReAct Prompt`: All the instructions, tools, output format, etc are passing in the prompt itself
2. `Tool Calling`: Use the [function calling](https://developers.openai.com/api/docs/guides/function-calling) functionality of LLMs (made available in June 2023) that also support the [structured output](https://developers.openai.com/api/docs/guides/structured-outputs)
3. `LangGraph ReAct Agent`: using function calling
4. `LangChain create_agent()`:using LangGraph ReAct agent
