# /v1/messages

## tools

```shell
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "What'\''s the latest on the Mars rover?"
      }
    ],
    "tools": [
      {
        "type": "web_search_20260209",
        "name": "web_search"
      }
    ]
  }'
```
