# Authentication

## OAuth 2.1

- Uses `Dynamic Client Registration` (RCR)

```shell
claude mcp add sentry https://mcp.sentry.dev/mcp \
  --transport http
```

## API Key Header

```shell
claude mcp add mymcp https://api.example.com/mcp \
  --transport http \
  --header "X-API-Key: sk_abc123"
```

## Pre-configured OAuth

```shell
claude mcp add mymcp https://mcp.example.com/mcp \
  --transport http \
  --client-id my-id \
  --client-secret my-secret \
  --callback-port 8080
```

## Stdio with env vars

```shell
claude mcp add github \
  --transport stdio
  --env GITHUB_TOKEN=ghp_xxx \
  -- npx -y @modelcontextprotocol/server-github
```
