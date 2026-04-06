# MCP

- Settings
  - **User scope**: `~/.claude.json` (.mcpServers)
  - **Local scope**: `~/.claude.json` (.projects.myproject.mcpServers)
  - **Project scope** `./.mcp.json` (.mcpServers)
  - **Managed scope**: `managed-mcp.json` in system directories (see Managed MCP configuration)

- Many cloud-based MCP servers require authentication. Claude Code supports OAuth 2.0 for secure connections, it should be done with the command `/mcp`

```json
{
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

## CLI

```shell
claude mcp list
claude mcp get "github"
claude mcp remove "github" -s local
```

```shell
# HTTP Server
claude mcp add github https://api.githubcopilot.com/mcp --transport http # same as --scope local
claude mcp add github https://api.githubcopilot.com/mcp --transport http --scope local # ~/.claude.json (.projects.<project>.mcpServers)
claude mcp add github https://api.githubcopilot.com/mcp --transport http --scope project # ./.mcp.json (.mcpServers)
claude mcp add github https://api.githubcopilot.com/mcp --transport http --scope user # ~/.claude.json (.mcpServers)

# Local stdio Server
claude mcp add mymcp /run.sh
claude mcp add clojure -- nu mcp server clojure --config-profile cli-assist-agent
claude mcp add airtable --transport stdio --env AIRTABLE_API_KEY=YOUR_KEY -- npx -y airtable-mcp-server
claude mcp add myserver --transport stdio --env KEY=value -- python server.py --port 8080

# SSE (Server-Sent Events) Server - this transport method is deprecated by MCP spec
claude mcp add asana https://mcp.asana.com/sse --transport sse --header "X-API-Key: your-key-here"

# From JSON (exactly how it will be added to the config file)
claude mcp add-json weather-api '{"type":"http","url":"https://api.weather.com/mcp","headers":{"Authorization":"Bearer token"}}'
```
