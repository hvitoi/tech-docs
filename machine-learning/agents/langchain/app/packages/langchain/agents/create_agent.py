from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


model = init_chat_model("google_genai:gemini-2.5-flash-lite")

agent = create_agent(
    model=model,  # you can specify the model string directly too (without building the model first)
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {
        "messages": [
            HumanMessage("What is the weather in San Francisco?"),
        ]
    }
)
print(result)
