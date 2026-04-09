from langchain.agents import create_agent
from langchain.agents.structured_output import ProviderStrategy
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from langchain.tools import BaseTool, tool
from pydantic import BaseModel, Field


# Structured Output
class AgentResponse(BaseModel):
    answer: str = Field(
        description="The agent's answer to the query",
    )
    magic_numbers: list[int] = Field(
        default_factory=list,
        description="A short list with random numbers",
    )


# Tools
@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"  # Just a hardcoded implementation, ideally it will go fetch the weather somewhere


tools: list[BaseTool] = [get_weather]

# Agent
llm = init_chat_model("anthropic:claude-sonnet-4-6")
agent = create_agent(
    model=llm,  # you can specify the model string directly too (without building the model first)
    response_format=ProviderStrategy(AgentResponse),
    tools=tools,
    system_prompt="You are a helpful assistant",
)


# Invoke
result = agent.invoke(
    {
        "messages": [
            HumanMessage("What is the weather in São Paulo?"),
        ]
    }
)

for msg in result["messages"]:
    print(f"[{msg.__class__.__name__}]: {msg.content}")
