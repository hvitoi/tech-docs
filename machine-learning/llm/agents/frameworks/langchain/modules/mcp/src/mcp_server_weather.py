from fastmcp import FastMCP

mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return "It's always sunny in New York"


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
        # other options: sse (deprecated by MCP spec), stdio
    )

# you can run it with "uv run src/mcp_server_weather.py"
