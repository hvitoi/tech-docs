from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ProviderStrategy
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from langchain.tools import tool
from pydantic import BaseModel, Field

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


class AgentResponse(BaseModel):
    answer: str = Field(
        description="The agent's answer to the query",
    )
    magic_numbers: list[int] = Field(
        default_factory=list,
        description="A short list with random numbers",
    )


model = init_chat_model("ollama:llama3.2")

agent = create_agent(
    model=model,  # you can specify the model string directly too (without building the model first)
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
    response_format=ProviderStrategy(AgentResponse),  # or the model directly
)

result = agent.invoke(
    {
        "messages": [
            HumanMessage("What is the weather in San Francisco?"),
        ]
    }
)
print(result)
