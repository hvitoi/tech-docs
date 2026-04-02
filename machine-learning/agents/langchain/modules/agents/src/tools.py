from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import BaseTool, tool


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"  # Just a hardcoded implementation, ideally it will go fetch the weather somewhere


tools: list[BaseTool] = [get_weather]

agent = create_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=tools,
)

result = agent.invoke(
    {
        "messages": [
            HumanMessage("What is the weather in São Paulo?"),
        ]
    }
)
for msg in result["messages"]:
    print(f"[{msg.__class__.__name__}]: {msg.content}")

# Workflow:
# 1. LangChain sends a request to LLM with the available tools and the user prompt
# 2. LLM answers with which tool to call and with which arguments
# 3. LangChain executes the tool define by the LLM
# 4. LangChain makes a new request to LLM with the tool result
# 5. LLM processes the input and decide that it already has a final solution, this final answer is returned
# 6. LangChain understand that the LLM decided that it is the final answer and return it to the client
