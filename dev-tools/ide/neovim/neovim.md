# Vim

- <https://github.com/neovim/neovim>

## Installation

```shell
brew install neovim
```

## Lua Scripting

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

## Packages

- `lazy`: plugin manager <https://github.com/folke/lazy.nvim>
- `telescope`: fuzzy filesystem finder <https://github.com/nvim-telescope/telescope.nvim>
