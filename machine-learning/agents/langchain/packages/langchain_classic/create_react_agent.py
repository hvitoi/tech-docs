from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_classic.agents import create_react_agent, AgentExecutor
from langsmith import Client

load_dotenv()

# The ReAct prompt:

# Answer the following questions as best you can. You have access to the following tools:
# {tools}
# Use the following format:
# Question: the input question you must answer
# Thought: you should always think about what to do
# Action: the action to take, should be one of [{tool_names}]
# Action Input: the input to the action
# Observation: the result of the action
# ... (this Thought/Action/Action Input/Observation can repeat N times)
# Thought: I now know the final answer
# Final Answer: the final answer to the original input question
# Begin!
# Question: {input}
# Thought:{agent_scratchpad}

langsmith_client = Client(api_url="https://eu.api.smith.langchain.com")
prompt = langsmith_client.pull_prompt("tseste/react")


@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's sunny in {city}."


tools = [get_weather]

llm = init_chat_model("ollama:llama3.2")

# The reasoning agent takes the prompt and send it to LLM
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

# # ... similar of what this would do
# chain = prompt | llm
# response = chain.invoke(
#     # Those are the required input variables
#     input={
#         "tools": "...",
#         "tool_names": "...",
#         "input": "What is your name?",
#         "agent_scratchpad": "...",
#     }
# )

# Then it the response of the LLM to the agent executor
# The executor is the orchestrator. It's responsible to call tools, runs another LLM call, etc
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)
chain = agent_executor

result = chain.invoke(input={"input": "What is the weather like in São Paulo?"})
print(result)
