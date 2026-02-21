from typing import Any

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult

load_dotenv()


class AgentCallbackHandler(BaseCallbackHandler):
    def on_llm_start(
        self,
        serialized: dict[str, Any],
        prompts: list[str],
        **kwargs: Any,
    ) -> Any:
        print("---LLM Request Prompt---")
        print(prompts[0])
        print("------------------------")

    def on_llm_end(
        self,
        response: LLMResult,
        **kwargs: Any,
    ) -> Any:
        print("---LLM Response---")
        print(response.generations[0][0].text)
        print("------------------")


llm = init_chat_model(
    "ollama:llama3.2",
    callbacks=[AgentCallbackHandler()],
)


response = llm.invoke("hey!")
