# Vim

- <https://github.com/neovim/neovim>

## Installation

```shell
brew install neovim
```

## Scripting

- **Init Script**
  - `~/.config/nvim/init.vim` (vim script)
  - `~/.config/nvim/init.lua` (lua)

- From the init script you can require any other packages inside the `lua` directory

```lua
-- ~/.config/nvim/init.lua
require("config.lazy") -- imports ~/.config/nvim/lua/config/lazy.lua
require("config") -- imports ~/.config/nvim/lua/config/init.lua
print("hello")
```

### Meta-accessors

- Functions that expose vim's low level APIs to the Lua runtime

```lua
-- Command
vim.cmd("set tabstop=2")

-- Option
vim.opt.tabstop = 2
vim.opt.expandtab = true

-- g
vim.g.mapleader = " "

-- Function
vim.fn.stdpath("data") -- ~/.local/share/nvim

-- Key Mapping
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)
```

## Netrw

- Default filetree explorer

- `%`: create new file
- `d`: create new directory

```conf
:Explore
```

```conf
vim.cmd("let g:netrw_liststyle = 3")
```

## LSP Client

- It's LSP client is written in Lua

## Packages

- `telescope`: fuzzy filesystem finder
- `navarasu/onedark.nvim`
- `nvim-tree/nvim-web-devicons`

## Commands

- `Ex`: go to Netrw explorer in the directory of the currently opened file
- `so`: source the current vim file
