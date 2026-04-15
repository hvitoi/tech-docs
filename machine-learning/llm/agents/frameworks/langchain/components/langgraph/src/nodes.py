from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from langchain_core.messages import AnyMessage
from langchain_core.tools import tool
from langchain.chat_models import init_chat_model


## TOOL NODE
@tool
def triple(num: float) -> float:
    """
    param num: a number to triple
    returns: the triple of the input number
    """
    return float(num) * 3


tools = [triple]


llm = init_chat_model(
    model="gpt-5.4",
    temperature=0,
).bind_tools(tools)


# ToolNode is a node that execute tools
tool_node = ToolNode(tools)


## REASONING NODE

SYSTEM_MESSAGE = """
You are a helpful assistant that can use tools to answer questions.
"""


def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
    Run the agent reasoning node.
    """
    response = llm.invoke(
        [{"role": "system", "content": SYSTEM_MESSAGE}, *state["messages"]]
    )
    return {"messages": [response]}
