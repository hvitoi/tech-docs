# Claude Code

- <https://code.claude.com/docs/en/overview>

```shell
brew install --cask claude-code
```

## Configuration

- <https://code.claude.com/docs/en/settings#what-uses-scopes>

- `~/.claude/settings.json`: per-user config
- `.claude/settings.json`: project config

```shell
# Auth config can only be set via environment variables
export ANTHROPIC_BASE_URL="https://myhost.com/anthropic"
export ANTHROPIC_AUTH_TOKEN="..."
export ANTHROPIC_CUSTOM_HEADERS="x-llm-application-name:claude_code"
```

## Memory (CLAUDE.md)

- `~/.claude/CLAUDE.md` (user)
- `./CLAUDE.md` (project)

## Commands

- `/init`: create CLAUDE.md (similar to AGENTS.md)
- `/theme`
- `/login`: log-in to add new credentials (or use the ANTHROPIC_AUTH_TOKEN env)
- `/clear`: clear conversation history
- `/memory`: open the memory file
- `/config`
- `/permissions`

## CLI

```shell
claude # interactive mode in cwd

# Task
claude "fix the build error" # one-time task

# Prompt (-f)
claude -p "explain this $CONTEXT" # prompt
tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"

# Last conversation (-c)
claude -c

# MCP
claude mcp add nu-mcp $HOME/dev/nu/nu-mcp/run.sh --scope user

# Commit
claude commit # create a git commit
```
