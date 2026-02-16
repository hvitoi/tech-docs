from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"  # Just a hardcoded implementation, ideally it will go fetch the weather somewhere


agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    tools=[get_weather],
)

result = agent.invoke(
    {
        "messages": [
            HumanMessage("What is the weather in São Paulo?"),
        ]
    }
)
print(result)

# Workflow:
# 1. LangChain sends a request to LLM with the available tools and the user prompt
# 2. LLM answers with which tool to call and with which arguments
# 3. LangChain executes the tool define by the LLM
# 4. LangChain makes a new request to LLM with the tool result
# 5. LLM processes the input and decide that it already has a final solution, this final answer is returned
# 6. LangChain understand that the LLM decided that it is the final answer and return it to the client
