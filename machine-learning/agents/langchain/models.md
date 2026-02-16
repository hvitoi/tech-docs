# Models

- The models (LLMs from an AI provider) can be utilized in 2 ways:

  1. With agents
      - Using `langchain.agents.create_agent`

  2. Standalone: called outside of the agent loop for tasks like text generation, classification, etc
      - Using `langchain.chat_models.init_chat_model`
      - Using provider-specific classes langchain_google_genai.ChatGoogleGenerativeAI, langchain_openai.ChatOpenAI, etc

```shell
pip install langchain[openai]
pip install langchain[google-genai]
pip install langchain[ollama]

uv add langchain-openai
uv add langchain-google-genai
uv add langchain-ollama
```
