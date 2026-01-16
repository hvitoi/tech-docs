# Open AI

- Sam Altman worked at `Y Combinator` (a business incubator)
- With that business acumen, he got funding to OpenAI in 2015
- At first it was a non-profit organization
- In order to attract talents, the promise was that there was no need to generate profit
  - The opposite of Google was doing with DeepMind
  - This liberty proposal was important because AI researchers believe AI can be the greatest or worst invention of humanity, depending on how it is applied
  - `p(doom)`: probability of bad outcomes of AI
  - `Boomers`: AI can only bring good results
  - `Doomers`: AI will collapse and extinguish humanity
- When OpenAI became for profit
  - Sam Altman became CEO
  - Elon Musk was kicked out and founded xAI
  - Dario Amodei left and founded Anthropic

## API

- Create an API key (secret key) <https://platform.openai.com/api-keys>
  - `Project API key`: granular access to resources (preferred)
  - `User API key`: access to all projects

### Models

```shell
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPEN_API_KEY"
```

### Completions

```shell
curl -X POST \
  "https://api.openai.com/v1/chat/completions" \
  -H "Authorization: Bearer $OPEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {
        "role": "user",
        "content": "Hello, how are you?"
      }
    ],
    "temperature": 0.7
  }'
```

```json
"messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Explain quantum computing in simple terms"
      }
    ],
```

```json
{
  "id": "chatcmpl-xxxxxx",
  "object": "chat.completion",
  "created": 1234567890,
  "model": "gpt-3.5-turbo",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! I'm doing well. How can I assist you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 14,
    "total_tokens": 23
  }
}
```
