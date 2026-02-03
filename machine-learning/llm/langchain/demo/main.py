import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    model = ChatOpenAI(
        base_url=os.getenv("OPENAI_BASE_URL"),  # if not specified, uses env OPENAI_BASE_URL
        api_key=os.getenv("OPENAI_API_KEY"),  # if not specified, uses env OPENAI_API_KEY
        model="gpt-5.2",
    )

    messages = [
        ("system", "You are a helpful assistant."),
        ("user", "Tell me a joke about programming."),
    ]

    response = model.invoke(messages)

    print("\n" + "=" * 50)
    print("Response:")
    print("=" * 50)
    print(response.content)
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
