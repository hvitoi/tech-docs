# Claude Code

- <https://code.claude.com/docs/en/overview>
- Claude Code is an agentic assistant that runs in your terminal.
- Claude Code serves as the `agentic harness` around Claude LLM: it provides the `tools`, `context management`, and `execution environment` that turn a language model into a capable coding agent
- Subscriptions: Pro, Max, Teams, or Enterprise. Or Claude Console (pre-paid credits)

```shell
brew install --cask claude-code
```

## Configuration

- <https://code.claude.com/docs/en/settings#what-uses-scopes>

- **Global Settings**
  - `~/.claude/settings.json` (settings)
  - `~/.claude/CLAUDE.md` (memory)
  - `~/.claude/.credentials.json` (secrets)
  - `~/.claude.json` (App state, UI preferences, MCP servers) - Mostly managed through `/config` (rather than directly editing)

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

## Tools

- With tools Claude Code can act
  - read your code
  - edit files
  - run commands
  - search the web
  - interact with external services
- Each tool use returns information that `feeds back into the agentic loop`, informing Claude's next decision.

- Categories of built-in tools (base capabilities)
  - `File operations`: Read files, edit code, create new files, rename and reorganize
  - `Search`: Find files by pattern, search content with regex, explore codebases
  - `Execution`: Run shell commands, start servers, run tests, use git
  - `Web`: Search the web, fetch documentation, look up error messages
  - `Code intelligence`: See type errors and warnings after edits, jump to definitions, find references (requires code intelligence plugins)

- You can extend the base capabilities with
  - **Skills**: what claude knows
  - **MCP**: connect to external services
  - **Hooks**: automate workflows
  - **Subagents**: offload tasks

- `Plugins` are the packaging layer. A plugin bundles `skills`, `hooks`, `subagents`, and `MCP servers` into a single installable unit. Plugin skills are namespaced (like `/my-plugin:review`) so multiple plugins can coexist

## Commands

- `/help`: show all commands/
- `/login`: log-in to add new credentials (or use the ANTHROPIC_AUTH_TOKEN env)
- `/theme`
- `/clear`: clear conversation history
- `/model`: switch between models (claude models only)
- `/doctor`: diagnoses common issues with your installation
- `/config`
- `/help`

- `/init`: create CLAUDE.md (similar to AGENTS.md)
- `/agents`: helps you configure custom subagents
- `/memory`: open the memory file
- `/resume`: jump back to previous conversation. Same as "claude -r"
- `/compact`: define rules for the context window compactation, e.g., "/compact focus on the API changes"
- `/context`: check what is using space on the context window
- `/btw`: side question
- `/permissions`

## CLI

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

### mcp

- Scopes
  - `User` and `local` scope: ~/.claude.json (in the mcpServers field or under project paths)
  - `Project` scope: .mcp.json in your project root (checked into source control)
  - `Managed`: managed-mcp.json in system directories (see Managed MCP configuration)

- Many cloud-based MCP servers require authentication. Claude Code supports OAuth 2.0 for secure connections, it should be done with the command `/mcp`

```shell
claude mcp list
claude mcp get "github"
claude mcp remove "github" -s local
```

```shell
# Local stdio Server
claude mcp add --scope user clojure -- nu mcp server clojure --config-profile cli-assist-agent
claude mcp add nu-mcp $HOME/dev/nu/nu-mcp/run.sh
claude mcp add --transport stdio --env AIRTABLE_API_KEY=YOUR_KEY airtable -- npx -y airtable-mcp-server
claude mcp add --transport stdio --env KEY=value myserver -- python server.py --port 8080

# HTTP Server
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ # for the current project (cwd) only (local scope) - default behavior
claude mcp add --transport http --scope user github https://api.githubcopilot.com/mcp/ # for all the projects (user scope)

# SSE (Server-Sent Events) Server
claude mcp add asana --transport sse https://mcp.asana.com/sse --header "X-API-Key: your-key-here"

# From JSON (exactly how it will be added to the config file)
claude mcp add-json weather-api '{"type":"http","url":"https://api.weather.com/mcp","headers":{"Authorization":"Bearer token"}}'
```

```json
// ~/.claude.json
{ // ...
  "mcpServers": {
    "nu-mcp": {
      "type": "stdio",
      "command": "/Users/myself/mymcp/run.sh",
      "args": [],
      "env": {}
    },
    "atlassian": {
      "type": "sse",
      "url": "https://mcp.atlassian.com/v1/sse"
    },
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

### plugin

- <https://claude.com/plugins>
- By default, the marketplace `anthropics/claude-plugins-official` is enabled
- MCPs installed via plugins do NOT appear under `~/.claude.json` (mcpServers)

```shell
# Plugins
claude plugin list
claude plugin install "<name>@claude-plugins-official" # or /plugin install <name>@claude-plugins-official

# Marketplace
claude plugin marketplace list
claude plugin marketplace add "git@github.com:myorg/myrepo.git" # add to ~/.claude/settings.json (extraKnownMarketplaces.myorg-myrepo)
claude plugin marketplace update # update plugins list
```

### commit

```shell
# Git commit
claude commit
```
