from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage

# optionally pass the tools as second arg
llm = init_chat_model("anthropic:claude-sonnet-4-6")

agent = create_agent(
    model=llm,  # you can specify the model string directly too (without building the model first)
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {
        "messages": [
            HumanMessage("Tell me a joke."),
        ]
    }
)

for msg in result["messages"]:
    print(f"[{msg.__class__.__name__}]: {msg.content}")
