from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

load_dotenv()


search_tool = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # include_favicon=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
    # exclude_domains=None,
    # country=None
)


agent = create_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[search_tool],
)


result = agent.invoke(
    {
        "messages": [
            HumanMessage("Search for job postings for an AI engineer in Lisbon.")
        ],
    },
)

for msg in result["messages"]:
    print(f"[{msg.__class__.__name__}]: {msg.content}")
