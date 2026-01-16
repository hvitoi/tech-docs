# Opencode

- API keys are saved at `$HOME/.local/share/opencode/auth.json`

## Agent modes

- `Build`: RW
- `Plan`: Ready-only

## Commands

- `/connect`: add API keys for a new AI provider
- `/models`: list all models based on your configured providers

- `/init`: sends a prompt to analyze the codebase and create an AGENTS.md file

## CLI

### opencode auth

```shell
# if you select "Other", it will create a provider entry at ~/.config/opencode/opencode.json
# https://opencode.ai/docs/providers/#custom-provider
opencode auth login
```
