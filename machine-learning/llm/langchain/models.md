# Models

- The models (LLMs from an AI provider) can be utilized in 2 ways
  1. With agents
  2. Standalone: called outside of the agent loop for tasks like text generation, classification, etc

- The models can be initialized using:
  1. Using langchain.chat_models.init_chat_model
  1. Using provider-specific classes langchain_google_genai.ChatGoogleGenerativeAI, langchain_openai.ChatOpenAI, etc

## Installing

```shell
pip install "langchain[openai]"
pip install "langchain[google-genai]"

uv add langchain-openai
uv add langchain-google-genai
```
