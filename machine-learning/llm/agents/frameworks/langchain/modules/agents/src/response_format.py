from langchain.agents import create_agent
from langchain.agents.structured_output import ProviderStrategy
from langchain.messages import HumanMessage
from pydantic import BaseModel, Field
from langchain.tools import tool

# Uses the structured output LLM functionalities https://developers.openai.com/api/docs/guides/structured-outputs)


class AgentResponse(BaseModel):
    answer: str = Field(
        description="The agent's answer to the query",
    )
    magic_numbers: list[int] = Field(
        default_factory=list,
        description="A short list with random numbers",
    )


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model="anthropic:claude-sonnet-4-6",
    response_format=ProviderStrategy(AgentResponse),
    tools=[get_weather],
)

result = agent.invoke(
    {
        "messages": [
            HumanMessage("What is the weather in San Francisco?"),
        ]
    }
)

for msg in result["messages"]:
    print(f"[{msg.__class__.__name__}]: {msg.content}")
