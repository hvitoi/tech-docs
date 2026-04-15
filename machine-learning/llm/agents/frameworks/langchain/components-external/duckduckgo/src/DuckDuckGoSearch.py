from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.messages import HumanMessage

search_tool = DuckDuckGoSearchResults(
    # max_results=5,
    # output_format="list",
)


agent = create_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[search_tool],
)


result = agent.invoke(
    {
        "messages": [HumanMessage("Search for restaurants in Lisbon.")],
    },
)

for msg in result["messages"]:
    msg.pretty_print()
