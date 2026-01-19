# Claude Code

- <https://code.claude.com/docs/en/overview>

```shell
brew install --cask claude-code
```

## Configuration

- Claude does not have config files! It uses environment variables only

```shell
export ANTHROPIC_BASE_URL="https://myhost.com/anthropic"
export ANTHROPIC_AUTH_TOKEN="..."
export ANTHROPIC_CUSTOM_HEADERS="x-llm-application-name:claude_code"
```

## Commands

- `/init`: create CLAUDE.md (similar to AGENTS.md)
- `/theme`

## CLI

```shell
claude # start in cwd
claude -p "explain this $CONTEXT" # prompt

# Add MCP
claude mcp add nu-mcp $HOME/dev/nu/nu-mcp/run.sh --scope user
```
