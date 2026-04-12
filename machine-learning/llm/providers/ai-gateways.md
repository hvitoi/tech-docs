# AI Gateways

## OpenRouter

- It's not a provider, but behaves like one
- It's a unified interface for LLMs. Offers a standard API format (OpenAI-compatible)
- Adopts a single interface (e.g., for authentication, billing, error, etc)
- <https://openrouter.ai/>

## LiteLLM

- <https://github.com/BerriAI/litellm>
- <https://docs.litellm.ai/docs/>
- Offers a standard API format (OpenAI-compatible)

```python
from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = "your-openai-key"
os.environ["ANTHROPIC_API_KEY"] = "your-anthropic-key"

# OpenAI
response = completion(model="openai/gpt-4o", messages=[{"role": "user", "content": "Hello!"}])

# Anthropic
response = completion(model="anthropic/claude-sonnet-4-20250514", messages=[{"role": "user", "content": "Hello!"}])
```

```shell
# ~/.zshrc
export LITELLM_API_KEY='...'
export LITELLM_BASE_URL='https://mylitellm.com'

# Anthropic
export ANTHROPIC_BASE_URL="$LITELLM_BASE_URL/anthropic" # proxy to anthropic
export ANTHROPIC_API_KEY="$LITELLM_API_KEY"
curl "$ANTHROPIC_BASE_URL/v1/models" -H "x-api-key: $ANTHROPIC_API_KEY" -H "anthropic-version: 2023-06-01"

# OpenAI
export OPENAI_BASE_URL="$LITELLM_BASE_URL/openai" # proxy to openai
export OPENAI_API_KEY="$LITELLM_API_KEY"
curl "$OPENAI_BASE_URL/v1/models" -H "Authorization: Bearer $OPENAI_API_KEY"

# if you use LITELLM_BASE_URL it will use the LITELLM API directly (which is OpenAI compatible)
```
