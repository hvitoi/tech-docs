# AI Gateways

## OpenRouter

- It's not a provider, but behaves like one
- It's a unified interface for LLMs. Offers a standard API format (OpenAI-compatible)
- Adopts a single interface (e.g., for authentication, billing, error, etc)
- <https://openrouter.ai/>

## OpenCode Zen

- <https://opencode.ai/docs/zen>

## LiteLLM

- <https://github.com/BerriAI/litellm>
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
