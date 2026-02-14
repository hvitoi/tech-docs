# Model Context Protocol (MCP)

- Standardizes how AI systems (like LLMs) connect with external tools and data sources
- Launched by Anthropic in December 2024
- It's connector between the LLM models and the context in which it needs to operate (the outside world)
- Key features
  - Portability: You don't need to rewrite integrations for each LLM vendor.
  - Security: It standardizes permissions and sandboxing, so agents don't get unrestricted access.
  - Ecosystem: Third-party developers can build MCP "servers" (tools, connectors) that any AI app can use.

## Architecture

- `MCP Client`: The AI model or chat interface (Claude Desktop, VS Code plugin, etc.).
- `MCP Server`: The external tool/service you want the AI to access (e.g., GitHub repo, Postgres DB, Jira).
- `MCP Protocol`: Defines how the client and server exchange messages (structured JSON).

### Servers

- Databases
- APIs
- Filesystems: let's AI read/write project files
- Dev tools (like VS Code, GitHub, CI/CD)
- Other agents
