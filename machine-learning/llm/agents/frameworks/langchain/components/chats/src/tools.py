from langchain.chat_models import init_chat_model
from langchain.tools import BaseTool, tool


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"  # Just a hardcoded implementation, ideally it will go fetch the weather somewhere


tools: list[BaseTool] = [get_weather]


# Another way to bind tools
# However, it will just answer with the chosen tool and the input to it. It won't continue on the loop with actually calling it
# This will just add the tools to the request to the LLM (.tools on the request body)
llm = init_chat_model("anthropic:claude-sonnet-4-6")
llm_with_tools = llm.bind_tools(tools)
response = llm_with_tools.invoke("What is the weather in São Paulo?")

print(response.content)


# Workflow:
# 1. LangChain sends a request to LLM with the available tools and the user prompt
# 2. LLM answers with which tool to call and with which arguments
# 3. LangChain executes the tool define by the LLM
# 4. LangChain makes a new request to LLM with the tool result
# 5. LLM processes the input and decide that it already has a final solution, this final answer is returned
# 6. LangChain understand that the LLM decided that it is the final answer and return it to the client
