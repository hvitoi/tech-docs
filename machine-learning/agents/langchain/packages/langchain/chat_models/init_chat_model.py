from langchain.chat_models import BaseChatModel, init_chat_model
# https://reference.langchain.com/python/langchain/models/#langchain.chat_models.init_chat_model


model: BaseChatModel = init_chat_model(
    "ollama:llama3.2",
    # "ollama:gemma3:270m", # does not accept tools
    # "google_genai:gemini-2.5-flash-lite",
    # "gpt-5.2",
    # api_key=os.getenv("MY_API_KEY"),  # if not specified, uses env OPENAI_API_KEY, GOOGLE_API_KEY, etc
    temperature=0.9,  # The higher, the more it will drift off (daydream)
    # timeout=30,
    # max_tokens=1000,
)

response = model.invoke("hey!")
print(response.content)
