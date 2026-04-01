# Claude Code

- <https://code.claude.com/docs/en/overview>
- Claude Code is an agentic assistant that runs in your terminal.
- Claude Code serves as the `agentic harness` around Claude LLM: it provides the `tools`, `context management`, and `execution environment` that turn a language model into a capable coding agent
- Subscriptions: Pro, Max, Teams, or Enterprise. Or Claude Console (pre-paid credits)

```shell
brew install --cask claude-code
```

```shell
claude # interactive mode in cwd

# Start a conversation with a prompt (task)
claude "fix the build error" # Interactive
claude -p "explain this $CONTEXT" # (print) Non-interactive (print and exit - useful for pipes)
tail -f app.log | claude -p "Slack me if you see any anomalies appear in this log stream"

# Pick a conversation
claude -r # (resume) pick session from a list
claude -c # (continue) last session in cwd
claude -c --fork-session # fork the last session and leave the last intact
```

## Configuration

- <https://code.claude.com/docs/en/settings#what-uses-scopes>

- **Global Settings**
  - `~/.claude/settings.json` (settings)
  - `~/.claude/CLAUDE.md` (memory)
  - `~/.claude/.credentials.json` (secrets)
  - `~/.claude.json` (App state, UI preferences, MCP servers) - Mostly managed through `/config` (rather than directly editing). Can also be project-specific when placed at ".projects.<-project>.mcpServers"

- **Project Settings**
  - `.claude/settings.json` (settings)
  - `.claude/CLAUDE.md`, `CLAUDE.md` (memory)
  - `.mcp.json` (MCPs)

```shell
# Auth config can only be set via environment variables
export ANTHROPIC_BASE_URL="https://myhost.com/anthropic"
export ANTHROPIC_AUTH_TOKEN="..."
export ANTHROPIC_CUSTOM_HEADERS="x-llm-application-name:claude_code"
```

## Agentic Loop

- The `Agentic Loop` is composed of "Gather context", "Take action" & "Verify results"
  - You start the loop with your prompt and you can interrupt, steer or add context in the middle of the loop

- **Permission Modes**
  - `Default`: claude asks before file edits and shell commands
  - `Accept edits`: claude edits files without asking, still asks for commands (you can still allow specific commands at the config file so claude won't ask each time)
  - `Plan mode`: claude uses read-only tools only
  - "Shift+Tab" to switch modes

## Sessions

- Also know as conversations
- Sessions are tied to your current directory
- Sessions are ephemeral, it has no persistent memory between sessions
  - If you want Claude to know something across sessions, put it in your CLAUDE.md.

- **Context Window**
  - Holds your `conversation history`, `file contents`, `command outputs`, `CLAUDE.md`, `loaded skills`, and `system instructions`
  - As you work, context fills up and claude compacts it automatically (detailed instructions from early conversations may be lost)
  - Put persistent rules in CLAUDE.md
  - Use /context to see what's using space
  - Claude Sonnet for instance has a limit of 200k tokens
