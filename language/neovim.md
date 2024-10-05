# Vim

- <https://github.com/neovim/neovim>

## Installation

```shell
brew install neovim
```

## Scripting

- Scripting can be done using `vim script` or `lua`

- **Init Script**: `~/.config/nvim/init.vim` or `~/.config/nvim/init.lua`
- From the init script you can require any other packages inside the `lua` directory

```lua
-- ~/.config/nvim/init.lua
require("mydir") -- ~/.config/nvim/lua/mydir/init.lua
require("myfile") -- ~/.config/nvim/lua/myfile
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

--
vim.g.mapleader = " "

-- Key mapping
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)
```

## Netrw

- Default filetree explorer

- `%`: create new file
- `d`: create new directory

## LSP Client

- It's LSP client is written in Lua

## Plugin Manager

- `lazy.nvim`
  - It's the most common plugin manager for vim
  - <https://github.com/folke/lazy.nvim>

- `packer`
  - Deprecated

## Packages

- `telescope`: fuzzy filesystem finder
- `navarasu/onedark.nvim`
- `nvim-tree/nvim-web-devicons`

## Commands

- `Ex`: go to Netrw explorer in the directory of the currently opened file
- `so`: source the current vim file
