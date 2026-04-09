# Structured Output

- You can define how your answer will look like
- <https://docs.langchain.com/oss/python/langchain/structured-output>

```python
class AgentResponse(BaseModel):
    answer: str = Field(
        description="The agent's answer to the query",
    )
    magic_numbers: list[int] = Field(
        default_factory=list,
        description="A short list with random numbers",
    )

agent = create_agent(
    model="ollama:llama3.2",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
    response_format=AgentResponse,
)
```

- There are 2 strategies
  - `Tool Strategy`: you use a local tool to structure the answer
  - `Provider Strategy`: you use the LLM to structure the answer natively
    - <https://developers.openai.com/api/docs/guides/structured-outputs>
    - Supported only by some providers/models. E.g., OpenAI, Anthropic (Claude), or xAI (Grok)
