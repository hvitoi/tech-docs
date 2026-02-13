from langchain.chat_models import init_chat_model


def main():
    # model = init_chat_model("gpt-5.2")
    model = init_chat_model("google_genai:gemini-2.5-flash-lite")

    # A single prompt
    response = model.invoke("Hi, how are you?")
    print(response.content)

    # A set of messages
    conversation = [
        {
            "role": "system",
            "content": "You are a helpful assistant that translates English to French.",
        },
        {"role": "user", "content": "Translate: I love programming."},
        {"role": "assistant", "content": "J'adore la programmation."},
        {"role": "user", "content": "Translate: I love building applications."},
    ]
    response = model.invoke(conversation)
    print(response.content)

    # see langchain.messages for more


if __name__ == "__main__":
    main()
