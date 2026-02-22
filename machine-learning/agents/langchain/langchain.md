# Langchain

- <https://docs.langchain.com/oss/python/langchain/overview> (you can copy it to input it to an LLM - see "llms.txt")
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

1. `ReAct Prompt with AgentExecutor` (2022~mid-2023)
    - `create_react_agent` & `AgentExecutor`
    - Prompt with the reasoning format (Thought/Action/Observation), tool descriptions and output instructions
    - The AgentExecutor ran the loop: call LLM, parse output, tool calls, append observations, repeat
2. `Tool Calling with AgentExecutor` (mid-2023~2024)
    - `create_tool_calling_agent` & `AgentExecutor`
    - OpenAI introduced function calling (June 2023)
    - Use the [function calling](https://developers.openai.com/api/docs/guides/function-calling) functionality of LLMs (made available in June 2023) that also support the [structured output](https://developers.openai.com/api/docs/guides/structured-outputs)
    - AgentExecutor still orchestrated the loop
3. `Tool Calling with LangGraph`
    - `create_agent` (langchain 1.0)
    - LangGraph allowed agents with graphs/state machines, not hidden loops
