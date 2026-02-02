# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "openai>=2.16.0",
# ]
# ///
from openai import OpenAI

client = OpenAI(
    api_key="<your-api-key>",
    base_url="<https://myhost.com>",
)

response = client.responses.create(
    model="gpt-5.2", input="Write a short bedtime story about a unicorn."
)
print(response)

response = client.chat.completions.create(
    model="gpt-5.2", messages=[{"role": "user", "content": "Hello!"}]
)
print(response)
