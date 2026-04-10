from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import ToolMessage

from ingestion import vector_store


@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve relevant documentation to help answer user queries about LangChain."""
    retrieved_docs = vector_store.as_retriever(search_kwargs={"k": 4}).invoke(query)

    serialized = "\n\n".join(
        f"Source: {doc.metadata.get('source', 'Unknown')}\n\nContent: {doc.page_content}"
        for doc in retrieved_docs
    )

    return serialized, retrieved_docs


system_prompt = (
    "You are a helpful AI assistant that answers questions about LangChain documentation. "
    "You have access to a tool that retrieves relevant documentation. "
    "Use the tool to find relevant information before answering questions. "
    "Always cite the sources you use in your answers. "
    "If you cannot find the answer in the retrieved documentation, say so."
)

agent = create_agent(
    "openai:gpt-5.4",
    tools=[retrieve_context],
    system_prompt=system_prompt,
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "what are deep agents?"}]}
)

answer = response["messages"][-1].content

context_docs = []
for message in response["messages"]:
    if isinstance(message, ToolMessage) and hasattr(message, "artifact"):
        if isinstance(message.artifact, list):
            context_docs.extend(message.artifact)

print(answer)
print(context_docs)
