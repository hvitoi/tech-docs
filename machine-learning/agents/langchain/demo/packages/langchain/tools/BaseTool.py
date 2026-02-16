from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import BaseTool, tool


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


tools: list[BaseTool] = [get_weather]

agent = create_agent(
    model="ollama:llama3.2",
    tools=tools,
)

result = agent.invoke(
    {
        "messages": [
            HumanMessage("What is the weather in São Paulo?"),
        ]
    }
)
print(result)
