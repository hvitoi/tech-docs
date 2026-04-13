# Github

- <https://github.com/github/github-mcp-server>

## PAT Authentication

- Your access token can be a `PAT` (long-lived) or an `App Token` (1-hour)

```json
{
  "type": "http",
  "url": "https://api.githubcopilot.com/mcp",
  "headers": {
    "Authorization": "Bearer <ACCESS_TOKEN>"
  }
}
```

## OAuth Authentication

- The Github MCP currently doesn't implement `Dynamic Client Registration (DCR)` (which is what MCP spec expects for OAuth)
- Therefore it's not possible to connect via OAuth with generic MCP Clients (e.g., Claude Code). You'd get the following error:

```txt
Error: SDK auth failed: Incompatible auth server: does not support dynamic client registration
```

- Instead, it uses a pre-registered OAuth App that's baked into specific clients.
- On VS Code it works because Microsoft pre-registered the OAuth credentials (client ID + secret) directly inside VS Code's codebase (for versions >=1.101)
- In other works, VSCode is responsible for generating the "installation token" (of an installed app) based on a private key (pem) and generate/refresh the access token when expired
