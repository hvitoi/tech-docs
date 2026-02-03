import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()


def main():
    model = init_chat_model(
        "gpt-5.2",
        api_key=os.getenv("OPENAI_API_KEY"),  # if not specified, uses env OPENAI_API_KEY
        temperature=0.7,
        timeout=30,
        max_tokens=1000,
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
