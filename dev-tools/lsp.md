# Language Server Protocol

- The `Language Server Protocol` (LSP) defines the protocol used between an editor and a language server that provides language features
  - `autocomplete`
  - `goto definition`
  - `documentation on hover`
  - etc
- <https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/>
- Clients (development tools) communicate with the server using the language protocol over `JSON-RPC`

## Language Server

- A `Language Server` is an external process with language specific rules

- Examples
  - rust-analyzer
  - gopls
  - tsserver (executed by the node language runtime)
  - html
  - cssls
  - tailwindcss
  - svelte
  - lua_ls
  - graphql
  - emmet_ls
  - prismals
  - pyright

## Language Client

- Your code editor

- Examples
  - vscode
