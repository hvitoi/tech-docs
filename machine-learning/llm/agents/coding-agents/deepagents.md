# Deep Agents

- <https://github.com/langchain-ai/deepagents>
- <https://docs.langchain.com/oss/python/deepagents/cli/overview>

- It's a new project in the Langchain umbrella
- It's basically a more rich agent with more capabilities
- Deep Agents solve the problem of an increasingly context. Because it delegates tasks and offload unnecessary context

- It's an `Agent Harness` (and agent general purpose client), not a framework like langchain

- Those capabilities/techniques mainly involve
  - `Planning Tool`: e.g., checklists
  - `Sub Agents`: sub instances of agents for specialized tasks
  - `File System`
  - `System Prompt`

## Configuration

- `~/.deepagents/config.toml`

## Install

```shell
# install globally
uv tool install 'deepagents-cli[ollama,groq]'
```

## Usage

```shell
# Run it (uses a default agent)
deepagents

# Prompt
git diff | deepagents --skill code-review -n 'summarize changes' # piped content appear first
deepagents -n "Generate a .gitignore for Python" -q > .gitignore

# Run your own agent
# the state (long term memory) for this agent will be stored (at ~/.deepagents/<myagent>/) and you can reopen it later on
deepagents --agent myagent

# List all agents created
deepagents agents list # default agent first
```

## Skills

- Deep agents have a `skills` framework
- Workflow
  1. Skills are loaded to the to the agent state on the session start
  2. Then, on each LLM call, the system prompt is updated with the skills metadata.
  3. Based on that, the LLM can request the read of the full skill when needed (progressive disclosure)

- Skills at `~/.agents/skills/` are read by deepagents
- It has the built-in skill `skill-creator`

```shell
npx skills add "remotion-dev/skills"
```

- You can ask deepagents which skills he has to verify
