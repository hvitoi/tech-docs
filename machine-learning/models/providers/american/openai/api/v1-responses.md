# /v1/responses

- This API is stateful, differently from chat completions API, which is stateless, in which you always needed to send the whole conversation every time
- In the Responses API, you don't always have to resend full history, OpenAI can manage conversation state internally
- Memory is no longer fully under your control
  - history may live on OpenAI's side
  - tool execution context may be hidden
  - you don't fully control what's stored or injected

- Most of the parameters from /v1/chat/completions work the same way in /v1/response (tools, response_format, stream, temperature, top_p, stop, etc). Only with a few unique parameters:

## input

- Differences in the Responses API:
  - `input` instead of `messages`
  - `instructions` field instead of a `system` role message
  - `max_output_tokens` instead of `max_tokens` / `max_completion_tokens`
  - flat tool schema (no nested `function` wrapper); the tool call comes back as an `output` item of `type: "function_call"`, and the result is sent back as a `function_call_output` item

### As simple text

```shell
# Input as a simple text
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5-nano",
    "input": "Tell me a joke."
  }'
````

```shell
# Continue the conversation with the ID received from the first response
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5-nano",
    "previous_response_id": "resp_abc123",
    "input": "Now make it funnier"
  }'
```

### Multimodal

```shell
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
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

## previous_response_id

- Reference a previous response
- No need to resend the full history

```shell
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4.1",
    "previous_response_id": "resp_abc123",
    "input": "Explain that more simply."
  }'
```

## tools

```shell
# Function calling: flat tool schema
curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5",
    "input": [
      { "role": "user", "content": "What is my horoscope? I am an Aquarius." }
    ],
    "tools": [
      {
        "type": "function",
        "name": "get_horoscope",
        "description": "Get todays horoscope for an astrological sign.",
        "parameters": {
          "type": "object",
          "properties": {
            "sign": { "type": "string" }
          },
          "required": ["sign"]
        }
      }
    ]
  }'
```

```json
// Tool call comes back as an output item; send the result back as function_call_output
{
  "output": [
    {
      "type": "function_call",
      "name": "get_horoscope",
      "call_id": "call_abc123",
      "arguments": "{\"sign\":\"Aquarius\"}"
    }
  ]
}
```
