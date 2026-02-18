from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel, Field

load_dotenv()


## OUTPUT STRUCTURE
class FinalResponse(BaseModel):
    city: str = Field(
        description="The city inputted.",
    )
    weather: str = Field(
        description="The weather for that city",
    )


output_parser = PydanticOutputParser(pydantic_object=FinalResponse)


# PROMPT

# langsmith_client = Client(api_url="https://eu.api.smith.langchain.com")
# react_prompt = langsmith_client.pull_prompt("tseste/react") # The original ReAct prompt from Langsmith Hub
react_prompt = PromptTemplate(
    template="""
        Answer the following questions as best you can. You have access to the following tools:

        {tools}

        Use the following format:

        Question: the input question you must answer
        Thought: you should always think about what to do
        Action: the action to take, should be one of [{tool_names}]
        Action Input: the input to the action
        Observation: the result of the action
        ... (this Thought/Action/Action Input/Observation can repeat N times)
        Thought: I now know the final answer
        Final Answer: the final answer to the original input question formatted according to format_instructions: {format_instructions}

        Begin!

        Question: {input}
        Thought:{agent_scratchpad}
        """,
    input_variables=[
        "tools",
        "tool_names",
        "format_instructions",
        "input",
        "agent_scratchpad",
    ],
)

react_prompt = react_prompt.partial(
    format_instructions=output_parser.get_format_instructions()
)

print(react_prompt)


# TOOLS
@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's sunny in {city}!"


tools = [get_weather]


## LLM
llm = init_chat_model("google_genai:gemini-2.5-flash")
# if a less capable model is used here (e.g., gemini 2.5 flash lite) then the agentic loop may run indefinitely without a final answer


## AGENT
# The reasoning agent takes the prompt and send it to LLM
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt,
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

extract_output = RunnableLambda(lambda result: output_parser.parse(result["output"]))

chain = agent_executor | extract_output

result = chain.invoke(input={"input": "What is the weather like in São Paulo today?"})
print(result)
