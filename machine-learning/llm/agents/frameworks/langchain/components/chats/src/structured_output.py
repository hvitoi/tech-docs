from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field

# Uses the structured output LLM functionalities (https://developers.openai.com/api/docs/guides/structured-outputs)


class ChatResponse(BaseModel):
    answer: str = Field(
        description="The answer to the query",
    )
    magic_numbers: list[int] = Field(
        default_factory=list,
        description="A short list with random numbers",
    )


llm = init_chat_model("anthropic:claude-sonnet-4-6")
llm_with_steroids = llm.with_structured_output(ChatResponse)

result = llm_with_steroids.invoke("What is the secret to happiness?")
print(result)
