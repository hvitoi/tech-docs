# Tools

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
