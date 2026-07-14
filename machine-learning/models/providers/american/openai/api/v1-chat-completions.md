# /v1/chat/completions

- It's a stateless API, the history has to be sent over in the next message

## messages

```shell
curl -X POST \
  "https://api.openai.com/v1/chat/completions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
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
    "temperature": 0.7
  }'
```

```json
// response
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

## tools

- You can provide a list of tools that the model can decide to use
- This is specially useful for agents
- In chat completions the tool is nested under a `function` object (in `/v1/responses` the schema is flat)
- <https://developers.openai.com/api/docs/guides/function-calling>
- <https://openai.com/index/function-calling-and-other-api-updates/> (released in June 13, 2023)

```shell
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {
        "role": "user",
        "content": "What is my horoscope? I am an Aquarius."
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_horoscope",
          "description": "Get todays horoscope for an astrological sign.",
          "parameters": {
            "type": "object",
            "properties": {
              "sign": {
                "type": "string",
                "description": "An astrological sign like Taurus or Aquarius"
              }
            },
            "required": ["sign"]
          }
        }
      }
    ]
  }'
```

```json
// The LLM tells which tool to use with which arguments (under tool_calls)
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "tool_calls": [
          {
            "id": "call_abc123",
            "type": "function",
            "function": {
              "name": "get_horoscope",
              "arguments": "{\"sign\":\"Aquarius\"}"
            }
          }
        ]
      },
      "finish_reason": "tool_calls"
    }
  ]
}
```

```python
def call_function(name, args):
  if name == "get_weather":
    return get_weather(**args)
  if name == "send_email":
    return send_email(**args)

for tool_call in response.choices[0].message.tool_calls:
  name = tool_call.function.name
  args = json.loads(tool_call.function.arguments)
  result = call_function(name, args)
  messages.append({
    "role": "tool",
    "tool_call_id": tool_call.id,
    "content": str(result)
  })
```

```json
// Send the result back with a "tool" role message, referencing the call id
"messages": [
  { "role": "user", "content": "What is my horoscope? I am an Aquarius." },
  {
    "role": "assistant",
    "tool_calls": [
      {
        "id": "call_abc123",
        "type": "function",
        "function": { "name": "get_horoscope", "arguments": "{\"sign\":\"Aquarius\"}" }
      }
    ]
  },
  {
    "role": "tool",
    "tool_call_id": "call_abc123",
    "content": "{\"horoscope\":\"Aquarius: Next Tuesday you will befriend a baby otter.\"}"
  }
]
```

```json
// And the model responds with the final answer
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Aquarius: Next Tuesday you will befriend a baby otter."
      },
      "finish_reason": "stop"
    }
  ]
}
```

## response_format

- <https://developers.openai.com/api/docs/guides/structured-outputs>
- The response format lets you control the shape of the model's output
- It's good to get reliable JSON to parse in your agent code

```shell
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "messages": [
      { "role": "user", "content": "Extract the user info: Hi, Im Sarah. Im 27 and live in Berlin. I like painting and cycling." }
    ],
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
// Model response (as the message content)
{
  "name": "Sarah",
  "age": 27,
  "city": "Berlin",
  "hobbies": ["painting","cycling"]
}
```

## instructions (system prompt)

- Good to set the tone, role and guardrails
- In chat completions this is a message with `role: "system"` (in `/v1/responses` it's the `instructions` field)

```shell
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "messages": [
      { "role": "system", "content": "You are a concise assistant. Reply in under 20 words." },
      { "role": "user", "content": "Explain photosynthesis." }
    ]
  }'
```

## max_tokens

- Prevents long answers and controls cost
- `max_tokens` is deprecated for newer/reasoning models in favor of `max_completion_tokens` (in `/v1/responses` it's `max_output_tokens`)

```shell
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "messages": [
      { "role": "user", "content": "Explain quantum computing simply." }
    ],
    "max_tokens": 50
  }'
```

## stream

- Tokens arrive as generated

```shell
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "messages": [
      { "role": "user", "content": "Tell a short story about space." }
    ],
    "stream": true
  }'
```

```json
data: { "choices": [{ "delta": { "content": "Once" } }] }
data: { "choices": [{ "delta": { "content": " upon" } }] }
data: { "choices": [{ "delta": { "content": " a time..." } }] }
```

## temperature

- Creativity control:
  - Lower: predictable
  - Higher: creative

- 0.2 factual/consistent
- 0.7 balanced
- 1.0+ creative (may cause hallucinations)

```shell
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "messages": [
      { "role": "user", "content": "Write a tagline for a coffee shop." }
    ],
    "temperature": 1.2
  }'
```

## top_p

- `Top P` (0 to 1)
  - Low P (e.g., 0.25) - safer
  - High P (e.g., 0.99): more broad answers, diverse output
- `Top K`
  - Low K (e.g., 10): more coherent responses
  - High K (e.g., 500): more diverse and creative

- Considers only the P% most likely words
- Alternative to temperature

```shell
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "messages": [
      { "role": "user", "content": "Write a tweet about AI." }
    ],
    "top_p": 0.8
  }'
```

## reasoning_effort

- On reasoning models (o-series, GPT-5, ...) the `reasoning_effort` parameter controls how many internal reasoning tokens the model spends before answering
- Values: `minimal`, `low`, `medium` (default), `high`
- Higher effort → better on hard/multi-step problems, but slower and more expensive
- Reasoning tokens are billed as output tokens but are **not** returned in the response

```shell
curl -X POST \
  "https://api.openai.com/v1/chat/completions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "o3",
    "reasoning_effort": "medium",
    "messages": [
      {
        "role": "user",
        "content": "Explain quantum computing in simple terms"
      }
    ]
  }'
```

- The response `usage` breaks out reasoning tokens under `completion_tokens_details`

```json
"usage": {
  "prompt_tokens": 9,
  "completion_tokens": 250,
  "total_tokens": 259,
  "completion_tokens_details": {
    "reasoning_tokens": 200
  }
}
```

## stop

- Force generation to stop once a specific token is reached
- Tokens that signals that the model to stop generating output

```shell
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4.1",
    "messages": [
      { "role": "user", "content": "List 5 fruits:" }
    ],
    "stop": ["4."] # stops when it hits "4."
  }'
```
