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
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ # same as --scope local
claude mcp add --transport http --scope local github https://api.githubcopilot.com/mcp/ # ~/.claude.json (.projects.<project>.mcpServers)
claude mcp add --transport http --scope project github https://api.githubcopilot.com/mcp/ # ./.mcp.json (.mcpServers)
claude mcp add --transport http --scope user github https://api.githubcopilot.com/mcp/ # ~/.claude.json (.mcpServers)

# Local stdio Server
claude mcp add --scope user clojure -- nu mcp server clojure --config-profile cli-assist-agent
claude mcp add nu-mcp $HOME/dev/nu/nu-mcp/run.sh
claude mcp add --transport stdio --env AIRTABLE_API_KEY=YOUR_KEY airtable -- npx -y airtable-mcp-server
claude mcp add --transport stdio --env KEY=value myserver -- python server.py --port 8080

# SSE (Server-Sent Events) Server
claude mcp add asana --transport sse https://mcp.asana.com/sse --header "X-API-Key: your-key-here"

# From JSON (exactly how it will be added to the config file)
claude mcp add-json weather-api '{"type":"http","url":"https://api.weather.com/mcp","headers":{"Authorization":"Bearer token"}}'
```
