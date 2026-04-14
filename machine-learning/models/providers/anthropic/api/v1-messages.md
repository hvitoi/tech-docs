# /v1/messages

## messages

```shell
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "Hey!"}
    ]
  }'
```

```shell
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d "{
    \"model\": \"claude-sonnet-4-6\",
    \"max_tokens\": 1000,
    \"messages\": [
      {
        \"role\": \"user\",
        \"content\": [
          {\"type\": \"text\", \"text\": \"Analyze this PDF\"},
          {
            \"type\": \"document\",
            \"source\": {
              \"type\": \"base64\",
              \"media_type\": \"application/pdf\",
              \"data\": \"$(cat document.b64)\"
            }
          }
        ]
      }
    ]
  }"
```

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
