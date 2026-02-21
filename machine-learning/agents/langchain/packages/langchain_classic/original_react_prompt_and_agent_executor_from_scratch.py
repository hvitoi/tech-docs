from typing import Any

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_classic.agents.format_scratchpad import format_log_to_str
from langchain_classic.agents.output_parsers import ReActSingleInputOutputParser
from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import BaseTool, Tool, render_text_description, tool

load_dotenv()

REACT_PROMPT = """
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
      Final Answer: the final answer to the original input question

      Begin!

      Question: {input}
      Thought: {agent_scratchpad}
      """


class AgentCallbackHandler(BaseCallbackHandler):
    def on_llm_start(
        self,
        serialized: dict[str, Any],
        prompts: list[str],
        **kwargs: Any,
    ) -> Any:
        print("***LLM Request Prompt***")
        print(prompts[0])
        print("************************")

    def on_llm_end(
        self,
        response: LLMResult,
        **kwargs: Any,
    ) -> Any:
        print("***LLM Response***")
        print(response.generations[0][0].text)
        print("******************")


@tool
def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    print(f"get_text_length enter with {text=}")
    trimmed_text = text.strip("'\n").strip('"')

    return len(trimmed_text)


def find_tool_by_name(tools: list[Tool], tool_name: str) -> Tool:
    for tool in tools:
        if tool.name == tool_name:
            return tool
    raise ValueError(f"Tool with name {tool_name} not found")


if __name__ == "__main__":
    print("Welcome!")

    tools: list[BaseTool] = [get_text_length]

    prompt_template = PromptTemplate.from_template(template=REACT_PROMPT).partial(
        tools=render_text_description(tools),
        tool_names=", ".join([t.name for t in tools]),
    )

    llm = init_chat_model(
        model="google_genai:gemini-2.5-flash",
        # Stop generating once it reaches the "Observation" token. This way, it stops that the "Action Input" line
        stop=["\nObservation", "Observation"],
        callbacks=[AgentCallbackHandler()],
        temperature=0,
    )

    agent = (
        {
            "input": lambda x: x["input"],  # get "input" from the agent invokation
            "agent_scratchpad": lambda x: format_log_to_str(x["agent_scratchpad"]),
        }
        | prompt_template
        | llm
        | ReActSingleInputOutputParser()  # put the selected "tool" and the "tool_input" into a map
    )

    scratchpad = []

    llm_output: AgentAction | AgentFinish | None = None

    while not isinstance(llm_output, AgentFinish):
        llm_output = agent.invoke(
            {
                "input": "What is the length of the word: DOG",
                "agent_scratchpad": scratchpad,
            }
        )

        if isinstance(llm_output, AgentAction):
            tool = find_tool_by_name(tools, llm_output.tool)
            tool_input = str(llm_output.tool_input)

            observation = tool.func(tool_input)
            print(f"***Function calling: {observation=}")
            scratchpad.append((llm_output, str(observation)))

    print(llm_output.return_values)
