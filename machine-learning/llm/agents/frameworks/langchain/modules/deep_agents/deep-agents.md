# Deep Agents

- <https://docs.langchain.com/oss/python/deepagents/cli/overview>
- Store keys in `~/.deepagents/.env` so they're available in every project without per-shell exports

## Install

```shell
# install globally
uv tool install 'deepagents-cli[ollama,groq]'

# install for the project (on the venv)
uv add 'deepagents-cli[ollama,groq]'
```

```shell
# Run it
deepagents
```

## Skills

- Skills at `~/.agents/skills/` are read by deepagents
- It has the built-in skill `skill-creator`

```shell
npx skills add "remotion-dev/skills"
```

- You can ask deepagents which skills he has to verify
