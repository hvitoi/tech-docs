from langchain.chat_models import BaseChatModel, init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


def main():
    # using init function
    model: BaseChatModel = init_chat_model(
        "google_genai:gemini-2.5-flash-lite",  # "gpt-5.2",
    )

    # Using model class
    # model = ChatOpenAI(
    #     base_url=os.getenv("OPENAI_BASE_URL"),  # if not specified, uses env OPENAI_BASE_URL
    #     api_key=os.getenv("OPENAI_API_KEY"),  # if not specified, uses env OPENAI_API_KEY
    #     model="gpt-5.2",
    # )

    # model = ChatGoogleGenerativeAI(
    #     model="gemini-2.5-flash-lite",
    # )

    # model = ChatOllama(
    #     model="gpt-oss",
    #     temperature=0,
    # )

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
