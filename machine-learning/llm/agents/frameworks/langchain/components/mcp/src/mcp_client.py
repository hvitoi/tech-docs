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

    tools = await mcp_client.get_tools()
    agent = create_agent("claude-sonnet-4-6", tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )

    for msg in math_response["messages"]:
        msg.pretty_print()

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    )

    for msg in weather_response["messages"]:
        msg.pretty_print()

    ## STATEFUL SESSION

    async with (
        mcp_client.session("math") as math_session,
        mcp_client.session("weather") as weather_session,
    ):
        # Both MCPs servers are initialized here (calling the "initialize" method)
        math_tools = await load_mcp_tools(math_session)
        weather_tools = await load_mcp_tools(weather_session)
        agent = create_agent("claude-sonnet-4-6", math_tools + weather_tools)

        math_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
        )

        for msg in math_response["messages"]:
            msg.pretty_print()

        weather_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
        )

        for msg in weather_response["messages"]:
            msg.pretty_print()


if __name__ == "__main__":
    asyncio.run(main())
