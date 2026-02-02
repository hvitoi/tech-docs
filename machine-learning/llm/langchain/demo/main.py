from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()  # load .env into os.environ


def main():
    llm = ChatOpenAI(
        # base_url="http://localhost:4000",  # If not provided, automatically pick from OPENAI_BASE_URL
        # api_key=os.getenv("OPENAI_API_KEY"), # If not provided, automatically pick from OPENAI_API_KEY
        model="gpt-5.2",
    )

    messages = [
        ("system", "You are a helpful assistant."),
        ("user", "Tell me a joke about programming."),
    ]

    # response = llm.invoke("What is the capital of France?") # with no context
    response = llm.invoke(messages)  # with context from messages

    print(response.content)


if __name__ == "__main__":
    main()
