import openai

client = openai.OpenAI(api_key="<your-liteLLM-key>", base_url="<https://myhost.com>")
response = client.chat.completions.create(
    model="openai/gpt-4o", messages=[{"role": "user", "content": "Hello!"}]
)
