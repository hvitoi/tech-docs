import asyncio

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    mcp_client = MultiServerMCPClient(
        {
            "math": {
                "transport": "stdio",
                "command": "python",
                "args": [
                    "/Users/henrique.vitoi/Documents/tech-docs/machine-learning/llm/agents/frameworks/langchain/modules/mcp/src/mcp_server_math.py"
                ],
            },
            "weather": {
                "transport": "http",
                "url": "http://localhost:8000/mcp",
            },
        }
    )

    tools = await mcp_client.get_tools()
    agent = create_agent("claude-sonnet-4-6", tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )

    for msg in math_response["messages"]:
        print(f"[{msg.__class__.__name__}]: {msg.content}")

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    )

    for msg in weather_response["messages"]:
        print(f"[{msg.__class__.__name__}]: {msg.content}")


if __name__ == "__main__":
    asyncio.run(main())
