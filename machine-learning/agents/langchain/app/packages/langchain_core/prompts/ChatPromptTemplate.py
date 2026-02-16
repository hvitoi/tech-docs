from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

# https://reference.langchain.com/python/langchain_core/prompts/


def main():
    # Create template
    prompt_template = ChatPromptTemplate(
        [
            ("system", "You are a helpful AI bot. Your name is {name}."),
            ("human", "Hello, how are you doing?"),
            ("ai", "I'm doing well, thanks!"),
            ("human", "{user_input}"),
        ]
    )

    # Populate the template with values
    prompt = prompt_template.invoke(
        {
            "name": "Bob",
            "user_input": "What is your name?",
        }
    )
    # prompt = prompt_template.invoke("Bob") # if it had only one var

    model = init_chat_model("google_genai:gemini-2.5-flash-lite")
    response = model.invoke(prompt)
    print(response.content)


if __name__ == "__main__":
    main()
