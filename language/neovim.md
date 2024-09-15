# Vim

- <https://github.com/neovim/neovim>

## Installation

```shell
brew install neovim
```

## Scripting

- Scripting can be done using `vim script` or `lua`

- **Init Script**
  - `~/.config/nvim/init.vim` or `~/.config/nvim/init.lua`

```lua
vim.opt.tabstop = 2
vim.opt.expandtab = true
```

## LSP Client

- It's LSP client is written in Lua

## Packages

- `packer`: Package Manager
- `telescope`: fuzzy filesystem finder
- `navarasu/onedark.nvim`
- `nvim-tree/nvim-web-devicons`
