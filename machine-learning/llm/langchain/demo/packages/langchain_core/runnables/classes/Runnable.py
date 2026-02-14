from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable


def main():

    model = init_chat_model("google_genai:gemini-2.5-flash-lite")

    prompt_template = ChatPromptTemplate(
        [
            ("system", "You are a helpful AI bot. Your name is {name}."),
            ("human", "Hello, how are you doing?"),
            ("ai", "I'm doing well, thanks!"),
            ("human", "{user_input}"),
        ]
    )

    # Pipe together the prompt_template into the model and invoke
    chain: Runnable = prompt_template | model
    # chain: Runnable = prompt_template.__or__(model) # same

    response = chain.invoke(
        input={
            "name": "Bob",
            "user_input": "What is your name?",
        }
    )

    print(response.content)


if __name__ == "__main__":
    main()
