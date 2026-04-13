# OAuth 2.1

<https://oauth.net/2.1/>

- **RFC 8414**": `Authorization Server Metadata`
  - Lets clients auto-discover endpoints (token URL, authorization URL, supported scopes, etc.) via a `.well-known/oauth-authorization-server` JSON document

- **RFC 7591**: `Dynamic Client Registration` (DCR)
  - Lets clients register themselves programmatically with the authorization server instead of being pre-registered manually.

## Flow (Authorization Code + PKCE + DCR)

- Example MCP server: <https://mcp.atlassian.com/v1/mcp/>

### 1. Initial request → 401

```shell
curl -X POST https://mcp.atlassian.com/v1/mcp/ \
  -H "Content-Type: application/json"

# HTTP/1.1 401 Unauthorized
```

### 2. Authorization Server Metadata Discovery (RFC 8414)

- Strip the path from the MCP URL to get the base domain

```shell
curl https://mcp.atlassian.com/.well-known/oauth-authorization-server \
  -H "MCP-Protocol-Version: 2024-11-05"
```

```json
{
  "issuer": "https://cf.mcp.atlassian.com",
  "authorization_endpoint": "https://mcp.atlassian.com/v1/authorize",
  "token_endpoint": "https://cf.mcp.atlassian.com/v1/token",
  "registration_endpoint": "https://cf.mcp.atlassian.com/v1/register",
  "response_types_supported": ["code"],
  "response_modes_supported": ["query"],
  "grant_types_supported": ["authorization_code", "refresh_token"],
  "token_endpoint_auth_methods_supported": ["client_secret_basic", "client_secret_post", "none"],
  "revocation_endpoint": "https://cf.mcp.atlassian.com/v1/token",
  "code_challenge_methods_supported": ["plain", "S256"]
}
```

### 3. Dynamic Client Registration (RFC 7591)

```shell
curl -X POST https://cf.mcp.atlassian.com/v1/register \
  -H "Content-Type: application/json" \
  -d '{
    "client_name": "My MCP Client",
    "redirect_uris": ["http://localhost:8080/callback"],
    "grant_types": ["authorization_code", "refresh_token"],
    "response_types": ["code"],
    "token_endpoint_auth_method": "none"
  }'
```

```json
{
  "client_id": "abc123-generated-client-id",
  "client_name": "My MCP Client",
  "redirect_uris": ["http://localhost:8080/callback"]
}
```

### 4. Generate PKCE parameters (local)

```shell
CODE_VERIFIER=$(openssl rand -base64 32 | tr -d '=+/' | cut -c1-43)
CODE_CHALLENGE=$(echo -n "$CODE_VERIFIER" | openssl dgst -sha256 -binary | base64 | tr '+/' '-_' | tr -d '=')
```

### 5. Authorization request (open in browser)

```shell
open "https://mcp.atlassian.com/v1/authorize\
  ?response_type=code\
  &client_id=abc123-generated-client-id\
  &redirect_uri=http://localhost:8080/callback\
  &code_challenge=$CODE_CHALLENGE\
  &code_challenge_method=S256\
  &scope=read:jira-work write:jira-work"
```

- User logs in and approves
- Browser redirects to `http://localhost:8080/callback?code=AUTHORIZATION_CODE`

### 6. Token exchange (code → access token)

```shell
curl -X POST https://cf.mcp.atlassian.com/v1/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code=AUTHORIZATION_CODE" \
  -d "redirect_uri=http://localhost:8080/callback" \
  -d "client_id=abc123-generated-client-id" \
  -d "code_verifier=$CODE_VERIFIER"
```

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "def456-refresh-token"
}
```

### 7. Authenticated MCP request

```shell
curl -X POST https://mcp.atlassian.com/v1/mcp/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIs..." \
  -d '{"jsonrpc": "2.0", "method": "tools/list", "id": 1}'
```

### 8. Token refresh (when access token expires)

```shell
curl -X POST https://cf.mcp.atlassian.com/v1/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=def456-refresh-token" \
  -d "client_id=abc123-generated-client-id"
```
