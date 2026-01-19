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

## Agent mode

- `Plan mode`: R-only
- `Accept edits`: RW

- "Shift+Tab" to switch modes

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

# Start a conversation with a prompt
claude "fix the build error" # Interactive
claude -p "explain this $CONTEXT" # (print) Non-interactive (print and exit - useful for pipes)
tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"

# Pick a conversation
claude -c # (continue) last conversation
claude -r # (resume) pick conversation from a list
```

### mcp

```shell
claude mcp add nu-mcp $HOME/dev/nu/nu-mcp/run.sh --scope user
```
