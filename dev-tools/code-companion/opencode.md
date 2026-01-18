# Opencode

- API keys are saved at `$HOME/.local/share/opencode/auth.json`

## Config Files

- `~/.config/opencode/opencode.json`: general config, including custom providers
- `~/.local/share/opencode/auth.json`: API keys

- <https://opencode.ai/docs/config/>

## Agents

- `Build`: RW
- `Plan`: Ready-only

- You can define custom agents using md files at `~/.config/opencode/agents/`

## Commands

- You can define custom commands using md files at `~/.config/opencode/commands/`

- `/commands`: (ctrl+p) show all commands

- `/connect`:  add API keys for a new AI provider
- `/models`:   (ctrl+x m) list all models based on your configured providers

- `/init`: sends a prompt to analyze the codebase and create an AGENTS.md file

## Providers

- Custom provider: <https://opencode.ai/docs/providers/#custom-provider>
- You can also select "Other" in the provider configuration and it will create an entry in the config file for you
- Custom providers use the libraries at <https://ai-sdk.dev/>

```json
// ~/.config/opencode/opencode.json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "myprovider": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "My AI ProviderDisplay Name",
      "options": {
        "baseURL": "https://api.myprovider.com/v1"
      },
      "models": {
        "my-model-name": {
          "name": "My Model Display Name"
        }
      }
    }
  }
}
```

## Context

- Type `@` on the chat for fuzzy searching in the project
- You can drag and drop images to the terminal too

## CLI

### opencode auth

```shell
opencode auth login # Add a new API Key
opencode auth list # Show all API Keys at the config file
```

### opencode web

- Create a web server to run opencode and expose it at <http://127.0.0.1:4096/>

```shell
opencode web
```

### opencode run

```shell
opencode run "Explain how closures work in JavaScript"
```
