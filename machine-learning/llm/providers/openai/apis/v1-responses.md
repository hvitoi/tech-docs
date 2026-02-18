# /v1/responses

## input

```shell
# Input as a simple text
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4.1",
    "input": "Tell me a joke."
  }'
```

```shell
# Multimodal input
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "input": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "What is in this image?"
          },
          {
            "type": "input_image",
            "image_url": "https://example.com/cat.jpg"
          }
        ]
      }
    ]
  }'
```

## tools

- You can provide a list of tools that the model can decide to use
- This is specially useful for agents

```shell
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4.1",
    "input": "What is the weather in Paris?",
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "Get current weather for a city",
          "parameters": {
            "type": "object",
            "properties": {
              "city": {
                "type": "string",
                "description": "City name"
              }
            },
            "required": ["city"]
          }
        }
      }
    ]
  }'
```

```json
// The LLM tells which tool to use with which arguments
{
  "id": "resp_123",
  "output": [
    {
      "type": "tool_call",
      "id": "call_001",
      "name": "get_weather",
      "arguments": "{\"city\":\"Paris\"}"
    }
  ]
}
```

```shell
# The agent can tell send back the result of the function call
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4.1",
    "input": [
      {
        "type": "tool_result",
        "tool_call_id": "call_001",
        "content": "{\"temp\":18,\"condition\":\"Cloudy\"}"
      }
    ]
  }'
```

```json
// And the model responds with the final answer
{
  "id": "resp_124",
  "output": [
    {
      "type": "message",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "The weather in Paris is 18°C and cloudy."
        }
      ]
    }
  ]
}
```

## response_format

- <https://developers.openai.com/api/docs/guides/structured-outputs>
- The response format lets you control the shape of the model's output
- It's good to get reliable JSON to parse in your agent code

```shell
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "input": "Extract the user info: Hi, Im Sarah. Im 27 and live in Berlin. I like painting and cycling.",
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "user_profile",
        "schema": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "age": { "type": "number" },
            "city": { "type": "string" },
            "hobbies": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["name","age","city","hobbies"],
          "additionalProperties": false
        }
      }
    }
  }'
```

```json
// Model response
{
  "name": "Sarah",
  "age": 27,
  "city": "Berlin",
  "hobbies": ["painting","cycling"]
}
```

## instructions

- Good to set the tone, role and guardrails
- It's a "system prompt"

```shell
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "instructions": "You are a concise assistant. Reply in under 20 words.",
    "input": "Explain photosynthesis."
  }'
```

## max_output_tokens

- Prevents long answers and controls cost

```shell
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "input": "Explain quantum computing simply.",
    "max_output_tokens": 50
  }'
```

## stream

- Tokens arrive as generated

```shell
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "input": "Tell a short story about space.",
    "stream": true
  }'
```

```json
data: { "delta": "Once" }
data: { "delta": " upon" }
data: { "delta": " a time..." }
```

## previous_response_id

- Reference a previous response
- No need to resend the full history

```shell
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "previous_response_id": "resp_abc123",
    "input": "Explain that more simply."
  }'
```

## temperature

- Creativity control:
  - Lower: predictable
  - Higher: creative

- 0.2 factual/consistent
- 0.7 balanced
- 1.0+ creative

```shell
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "input": "Write a tagline for a coffee shop.",
    "temperature": 1.2
  }'
```

## top_p

- Alternative to temperature
- Lower value = safer outputs

```shell
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "input": "Write a tweet about AI.",
    "top_p": 0.8
  }'
```

## stop

- Force generation to stop

```shell
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "input": "List 5 fruits:",
    "stop": ["4."] # stops when it hits "4."
  }'
```
