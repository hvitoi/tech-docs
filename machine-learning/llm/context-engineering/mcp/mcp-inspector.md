# MCP Inspector

- Helps troubleshooting a MCP server
- <https://modelcontextprotocol.io/docs/tools/inspector>
- <https://github.com/modelcontextprotocol/inspector>

```shell
npx @modelcontextprotocol/inspector # connect later to a mcp server e.g., https://docs.langchain.com/mcp
npx @modelcontextprotocol/inspector <command> # start a server stdio
```

## Exploring MCP with curl

- Remote MCP uses the `Streamable HTTP` transport: a single POST endpoint speaking JSON-RPC 2.0
- Responses come back as `text/event-stream` (SSE-framed): each message arrives as `event: message\ndata: {...json...}`
- Required headers on every POST:
  - `Content-Type: application/json`
  - `Accept: application/json, text/event-stream`
- Some servers issue an `Mcp-Session-Id` response header on `initialize` that must be echoed back on subsequent requests
- Handshake order: `initialize` → `notifications/initialized` (HTTP 202, no body) → any operation (`tools/list`, `tools/call`, ...)

### 1. Initialize

```shell
curl -s -X POST https://docs.langchain.com/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
      "protocolVersion": "2025-06-18",
      "capabilities": {},
      "clientInfo": {"name": "curl", "version": "0.1"}
    }
  }'
```

Server replies with its `protocolVersion`, advertised `capabilities` (tools/resources/prompts), and `serverInfo`.

### 2. Send the initialized notification

Notifications have no `id`; the server responds with `HTTP 202` and an empty body.

```shell
curl -s -X POST https://docs.langchain.com/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","method":"notifications/initialized"}'
```

### 3. List and call tools

```shell
# list tools
curl -s -X POST https://docs.langchain.com/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'

# call a tool
curl -s -X POST https://docs.langchain.com/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
      "name": "search_docs_by_lang_chain",
      "arguments": {"query": "what is langgraph"}
    }
  }'
```

Other useful methods: `resources/list`, `resources/read`, `prompts/list`, `prompts/get`, `ping`.
