# vi

- 1976: [vi](https://ex-vi.sourceforge.net/) by Bill Joy
- 1991: [vim](https://github.com/vim/vim) by Bram Moolenaar
- 2014: [neovim](https://github.com/neovim/neovim)

## Modes

- **Normal Mode**: `Esc`
- **Insert Mode**: `i`
- **Visual Mode**: `v`
- **Command Mode**: `:`

## Movement

- `h`: left
- `l`: right
- `k`: up
- `j`: down

- `0` or `^`: beginning of line
- `$`: end of line

- `w`: next word (first char)
- `ge`: previous word (last char)
- `e`: current word (last char) or next word (last char)
- `b`: current word (first char) or last word (first char)

- `f[char]`: next occurrence of a character. E.g., fz (next z)
- `F[char]`: previous occurrence of a character. E.g., fz (previous z)

- `*`: next occurrence of the word under cursor
- `#`: previous occurrence of the word under cursor

- `%`: alternate between opening and closing characters. E.g., ( and ), [ and ], { and }

- `gg`: go to first line
- `25%`: go to the line at 25% of the file
- `50%`: go to the line at 50% of the file
- `G`: go to last line
- `8G`: go to line number 8

- `{`: previous empty line
- `}`: next empty line

- `''`: return to the previous position

- `Ctrl` + `g`: shows current position
- `Ctrl` + `u`: half page up
- `Ctrl` + `d`: half page down

## Visual

- In visual model, you select text using movement keys before you decide what to do with it

- `v` stands for _visual selection_
- `V`: selects the whole line

- **Select around**
  - `vaw`: for word
  - `vap`: for paragraph
  - `va(`: for parenthesis

- **Select inside**
  - `viw`: for word
  - `vip`: for paragraph
  - `vi(`: for parenthesis

- `Ctrl+v`: block selection

> gg + 0 + v + G: selects the whole file

## Insert

- `i`: Insert mode at left of current selection
- `a`: Insert mode at right of current selection

- `I`: Insert mode at the beginning of line
- `A`: Insert mode at the end of line

- `o`: Insert mode at a new line (after)
- `O`: Insert mode at a new line (before)

- `S`: clear the current line and enter insert mode

## Delete

- `x`: delete character under cursor
- `X`: delete character to the left of cursor

- `D`: delete until end of line
- `dd`: delete the whole line

- **Delete movement**
  - `d[movement]`
  - When combining with movement command it will delete all the way through
  - Deleted text is registered in VIM (copied) so that it can be pasted afterwards
  - E.g., dw deletes from cursor to beginning of next word
  - E.g., d2e deletes from cursor to the end of next word

- **Delete around**: delete around the borders (whitespaces, parenthesis, etc)
  - `daw`: for word
  - `dap`: for paragraph
  - `da(`: for parenthesis

- **Delete inside**: delete only inside the borders
  - `diw`: for word
  - `dip`: for paragraph
  - `di(`: for parenthesis

## Change

- Same as delete, but additionally starts insert mode
- `c`

## Replace

- `r[char]`: replace one character
- `R`: replace mode (overwrite the text that's already there)

## Number powered

- Commands can be added any number multiplier in front of it
- `[n][action/movement]`

- Examples
  - 3w (next 3 words)
  - 3igo (insert gogogo)

## Yank (Copy)

- `y` copies from a command or visual selection
- `yy`: yank the whole line
- `yap`: copies the whole paragraph

## Put (Paste)

- Paste text in the current selection
- Text to be pasted must in vim's register
- vim does not have the ability from paste from you system clipboard

- `p`

## Period

- `.`: executes the last command

## Undo / Redo

- `u`: undo last operation
- `U`: undo whole line

- `ctrl + r`: Redo

## Focus

- `z + z`: Focus the current line (middle)
- `z + t`: Focus the current line (top)

## Macro

- `q + q`: record a macro. `q` again to stop macro recording
- `@ + q`: use the recorded macro

## Quit

- `Shift + Z + Z`: Save and Quit
- `Shift + Z + Q`: Quit without saving

## Search

- `/keyword`: search forwards
- `?keyword`: search backwards

- `n`: next occurrence
- `N`: previous occurrence

## Commands

### q

- `q`: quit

### w

- `:w`: save file
- `:w!`: save file (force)
- `:w !sudo tee %`: save file with sudo
- `:x`: save and quit

### s

- `:s/old/new`: replace first occurrence (only applicable for the current line)
- `:s/old/new/c`: prompts the substitute or not
- `:s/old/new/g`: replace all occurrences within the line
- `:%s/old/new/g`: replace all occurrences throughout the document

### r

- `:r !command`" paste output from a command

### e

- `:e ~/.vimrc`: start editing config file
- `:e ~/file.txt`: open a file

### \\

- `:!`: execute any shell command
- `:!ls`: execute any shell command
- `:!ps -ef`: execute any shell command

### sort

- `:sort`: sort the text selected

### earlier

- `:earlier 5m`: go to the state 5 minutes before

### later

- `:later 5m`: go to the state 5 minutes after

### norm

- `:norm .`: executes period (last command) for all lines selected

### set

- `:set hls`: set a variable called "hls" (highlight search)
- `:set ic`: set a variable called "ic" (ignore case)
- `:set paste`: allow paste from clipboard

### healthcheck

- `:healthcheck`

### help

- `:help`
- `:help nvim`
- `:help news`
- `:help rtp`: runtimepath help
