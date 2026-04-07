# Deep Agents

- <https://docs.langchain.com/oss/python/deepagents/cli/overview>
- It's an `Agent Harness` (and agent general purpose client), not a framework like langchain
- Store keys in `~/.deepagents/.env` so they're available in every project without per-shell exports

## Install

```shell
# install globally
uv tool install 'deepagents-cli[ollama,groq]'

# install for the project (on the venv)
uv add 'deepagents-cli[ollama,groq]'
```

## Usage

```shell
# Run it (uses a default agent)
deepagents

# Run your own agent
# the state (long term memory) for this agent will be stored (at ~/.deepagents/<myagent>/) and you can reopen it later on
deepagents --agent myagent

# List all agents created
deepagents list
```

## Skills

- Skills at `~/.agents/skills/` are read by deepagents
- It has the built-in skill `skill-creator`

```shell
npx skills add "remotion-dev/skills"
```

- You can ask deepagents which skills he has to verify
