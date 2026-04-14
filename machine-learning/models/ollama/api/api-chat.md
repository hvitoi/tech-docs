# /api/chat

## tools

```shell
curl -s http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{
        "model": "qwen3",
        "messages": [
          {
            "role": "user",
            "content": "What is the temperature in New York?"
          }
        ],
        "stream": false,
        "tools": [
          {
            "type": "function",
            "function": {
              "name": "get_temperature",
              "description": "Get the current temperature for a city",
              "parameters": {
                "type": "object",
                "required": ["city"],
                "properties": {
                  "city": {"type": "string", "description": "The name of the city"}
                }
              }
            }
          }
        ]
      }'
```

```shell
# Subsequent request with the tool result
curl -s http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{
        "model": "qwen3",
        "messages": [
          {
            "role": "user",
            "content": "What is the temperature in New York?"
          },
          {
            "role": "assistant",
            "tool_calls": [
              {
                "type": "function",
                "function": {
                  "index": 0,
                  "name": "get_temperature",
                  "arguments": {"city": "New York"}
                }
              }
            ]
          },
          {
            "role": "tool",
            "tool_name": "get_temperature",
            "content": "22°C"
          }
        ],
        "stream": false
      }'
```
