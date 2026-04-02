from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

# Model Class


# https://docs.langchain.com/oss/python/integrations/chat/anthropic
# uv add langchain-anthropic
llm = ChatAnthropic(
    model_name="claude-sonnet-4-6",
    timeout=60.0,
    stop=[],
    # temperature=,
    # max_tokens=,
    # max_retries=,
    # ...
)

# https://docs.langchain.com/oss/python/integrations/chat/openai
# uv add langchain-openai
# llm = ChatOpenAI(
#     model="gpt-5.2",
#     base_url=os.getenv("OPENAI_BASE_URL"),  # if not specified, uses env OPENAI_BASE_URL
#     api_key=os.getenv("OPENAI_API_KEY"),  # if not specified, uses env OPENAI_API_KEY
# )

# https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai
# uv add langchain-google-genai
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash-lite",
# )

# https://docs.langchain.com/oss/python/integrations/chat/ollama
# uv add langchain-ollama
# llm = ChatOllama(
#     model="gpt-oss",
# )

# A single prompt
response = llm.invoke("Hi, how are you?")
print(response.content)

# see langchain.messages for more
