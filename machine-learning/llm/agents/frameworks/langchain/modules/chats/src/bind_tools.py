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
