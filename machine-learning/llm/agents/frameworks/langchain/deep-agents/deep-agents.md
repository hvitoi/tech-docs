# Deep Agents

- <https://docs.langchain.com/oss/python/deepagents/cli/overview>
- <https://blog.langchain.com/deep-agents/>

- It's a new project in the Langchain umbrella
- It's basically a more rich agent with more capabilities

- It's an `Agent Harness` (and agent general purpose client), not a framework like langchain
- Store keys in `~/.deepagents/.env` so they're available in every project without per-shell exports
- Deep agents also have a `skills` framework, that are loaded upon demand

- Those capabilities/techniques mainly involve
  - `Planning Tool`: e.g., checklists
  - `Sub Agents`: sub instances of agents for specialized tasks
  - `File System`
  - `System Prompt`

- Deep Agents solve the problem of an increasingly context. Because it delegates tasks and offload unnecessary context

![Deep Agents](.images/deep-agents.png)

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
