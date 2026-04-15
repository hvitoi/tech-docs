from typing import Literal

from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage, ToolMessage
from langchain.tools import tool
from langgraph.graph import END, START, MessagesState, StateGraph


# --- Tools ---


@tool
def triple(num: float) -> float:
    """Triple a number.

    Args:
        num: a number to triple
    """
    return num * 3


tools = [triple]
tools_by_name = {t.name: t for t in tools}

# --- LLM ---

llm_with_tools = init_chat_model("openai:gpt-5.4", temperature=0).bind_tools(tools)

# --- Nodes ---


def llm_call(state: MessagesState):
    """LLM decides whether to call a tool or not."""
    return {
        "messages": [
            llm_with_tools.invoke(
                [
                    SystemMessage(
                        content="You are a helpful assistant that can use tools to answer questions."
                    )
                ]
                + state["messages"]
            )
        ]
    }


def tool_node(state: MessagesState):
    """Execute the tool calls from the last message."""
    results = []
    for tool_call in state["messages"][-1].tool_calls:
        observation = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        results.append(
            ToolMessage(content=str(observation), tool_call_id=tool_call["id"])
        )
    return {"messages": results}


# --- Routing ---


def should_continue(state: MessagesState) -> Literal["tool_node", "__end__"]:
    """Route to tool_node if the LLM made tool calls, otherwise end."""
    if state["messages"][-1].tool_calls:
        return "tool_node"
    return END


# --- Graph ---

graph = StateGraph(MessagesState)

graph.add_node("llm_call", llm_call)
graph.add_node("tool_node", tool_node)

graph.add_edge(START, "llm_call")
graph.add_conditional_edges("llm_call", should_continue, ["tool_node", END])
graph.add_edge("tool_node", "llm_call")

agent = graph.compile()
agent.get_graph().draw_mermaid_png(output_file_path="flow.png")

# --- Run ---

if __name__ == "__main__":
    result = agent.invoke({"messages": [HumanMessage(content="what is 100 *3?")]})
    for msg in result["messages"]:
        msg.pretty_print()
