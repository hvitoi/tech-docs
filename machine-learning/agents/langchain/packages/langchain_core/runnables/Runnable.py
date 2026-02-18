from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableLambda


# https://reference.langchain.com/python/langchain_core/runnables/#langchain_core.runnables.base.Runnable


model = init_chat_model("google_genai:gemini-2.5-flash-lite")

prompt_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful AI bot. Your name is {name}."),
        ("human", "Hello, how are you doing?"),
        ("ai", "I'm doing well, thanks!"),
        ("human", "{user_input}"),
    ]
)

do_something_else = RunnableLambda(lambda result: dict(result) | {"foo": "bar"})

# Pipe together the prompt_template into the model and invoke
chain: Runnable = prompt_template | model | do_something_else
# chain: Runnable = prompt_template.__or__(model) # same

result = chain.invoke(
    input={
        "name": "Bob",
        "user_input": "What is your name?",
    }
)

print(result)
