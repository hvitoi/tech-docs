# Open AI

- Create an API key (secret key) <https://platform.openai.com/api-keys>
  - `Project API key`: granular access to resources (preferred)
  - `User API key`: access to all projects

## API

### Models

```shell
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPEN_API_KEY"
```

### Completions

```shell
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPEN_API_KEY" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello, how are you?"}],
    "temperature": 0.7
  }'
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
