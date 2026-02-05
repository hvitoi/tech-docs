from langchain.chat_models import init_chat_model

# https://docs.langchain.com/oss/python/langchain/messages#text-prompts
# Text prompts are strings, ideal for straightforward generation tasks where you don't need to retain conversation history.


def main():
    model = init_chat_model("google_genai:gemini-2.5-flash-lite")
    response = model.invoke("Write a haiku about spring")
    print(response.content)


if __name__ == "__main__":
    main()
