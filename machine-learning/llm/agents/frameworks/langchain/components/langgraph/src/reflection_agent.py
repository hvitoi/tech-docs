from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import MessagesState

# https://blog.langchain.com/reflection-agents/

# --- Prompts ---

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influencer assistant tasked with writing excellent twitter posts."
            " Generate the best twitter post possible for the user's request."
            " If the user provides critique, respond with a revised version of your previous attempts.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet."
            " Generate critique and recommendations for the user's tweet."
            " Always provide detailed recommendations, including requests for length, virality, style, etc.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# --- Chains ---

llm = init_chat_model("openai:gpt-5.4", temperature=0.7)
generate_chain = generation_prompt | llm
reflect_chain = reflection_prompt | llm

# --- Nodes ---

MAX_REFLECTIONS = 3


def generate(state: MessagesState):
    """Generate or revise a tweet based on the conversation so far."""
    response = generate_chain.invoke({"messages": state["messages"]})
    return {"messages": [response]}


def reflect(state: MessagesState):
    """Critique the latest draft and return feedback as a HumanMessage."""
    # The AIMessage will appear as a HumanMessage. It's like the Human is reflecting about the previous AI Message (the generation). But in fact it's AI criticizing itself
    response = reflect_chain.invoke({"messages": state["messages"]})
    return {"messages": [HumanMessage(content=response.content)]}


# --- Routing ---


# Quit after 3 reflections
def should_continue(state: MessagesState) -> str:
    """Stop after MAX_REFLECTIONS rounds (each round = generate + reflect = 2 messages)."""
    if len(state["messages"]) > MAX_REFLECTIONS * 2:
        return END
    return "reflect"


# --- Graph ---

graph = StateGraph(MessagesState)

graph.add_node("generate", generate)
graph.add_node("reflect", reflect)

graph.add_edge(START, "generate")
graph.add_conditional_edges("generate", should_continue, ["reflect", END])
graph.add_edge("reflect", "generate")

agent = graph.compile()
agent.get_graph().draw_mermaid_png(output_file_path="reflection-agent-flow.png")

# --- Run ---

if __name__ == "__main__":
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content=(
                        "Rewrite this rough draft into a viral tweet:\n\n"
                        "@LangChainAI — newly Tool Calling feature is seriously underrated. "
                        "After a long wait, it's here — making the implementation of agents "
                        "across different models with function calling super easy. "
                        "Made a video covering their newest blog post."
                    )
                )
            ]
        }
    )
    for msg in result["messages"]:
        msg.pretty_print()
