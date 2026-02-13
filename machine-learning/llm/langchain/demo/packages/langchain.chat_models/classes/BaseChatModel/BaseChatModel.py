from langchain.chat_models import BaseChatModel, init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
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
    # model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

    response = model.invoke("hey!")
    print(response.content)


if __name__ == "__main__":
    main()
