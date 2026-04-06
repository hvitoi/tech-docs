import asyncio

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools


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
                "transport": "streamable_http",
                "url": "http://localhost:8000/mcp",  # this must be started beforehand
            },
        }
    )

    ## STATELESS SESSION

    # tools = await mcp_client.get_tools()
    # agent = create_agent("claude-sonnet-4-6", tools)

    # math_response = await agent.ainvoke(
    #     {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    # )

    # for msg in math_response["messages"]:
    #     print(f"[{msg.__class__.__name__}]: {msg.content}")

    # weather_response = await agent.ainvoke(
    #     {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    # )

    # for msg in weather_response["messages"]:
    #     print(f"[{msg.__class__.__name__}]: {msg.content}")

    ## STATEFUL SESSION
    async with mcp_client.session("math") as session:
        # this session contains only the "math" MCP
        # The MCP is initialized here (initialize method is called)

        tools = await load_mcp_tools(session)
        agent = create_agent("claude-sonnet-4-6", tools)

        math_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
        )

        for msg in math_response["messages"]:
            print(f"[{msg.__class__.__name__}]: {msg.content}")

        # This WON'T use weather MCP because it's not on the session
        weather_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
        )

        for msg in weather_response["messages"]:
            print(f"[{msg.__class__.__name__}]: {msg.content}")


if __name__ == "__main__":
    asyncio.run(main())
