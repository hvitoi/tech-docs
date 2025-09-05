# vi

- 1976: [vi](https://ex-vi.sourceforge.net/) by Bill Joy
- 1991: [vim](https://github.com/vim/vim) by Bram Moolenaar
- 2014: [neovim](https://github.com/neovim/neovim)

## Modes

- **Normal Mode**
- **Insert Mode**
- **Visual Mode**
- **Command Mode**
- **Replace Mode**

## Visual

- In visual model, you select text using movement keys before you decide what to do with it

- `v` stands for _visual selection_
- `V`: selects the whole line

- `Ctrl+v`: block selection

## Insert

- `i`: Insert mode at left of current selection
- `a`: Insert mode at right of current selection

- `I`: Insert mode at the beginning of line
- `A`: Insert mode at the end of line

- `o`: Insert mode at a new line (after)
- `O`: Insert mode at a new line (before)

- `S`: clear the current line and enter insert mode

## Delete

- Deleted text is registered in VIM (copied) so that it can be pasted afterwards

- `x`: delete character under cursor
- `X`: delete character to the left of cursor

- `D`: delete until end of line
- `dd`: delete the whole line

## Change

- Same as delete, but additionally starts insert mode
- `c`

## Replace

- `r[char]`: replace one character
- `R`: replace mode (overwrite the text that's already there)

## Yank (Copy)

- `y` copies from a command or visual selection
- `yy`: yank the whole line
- `yap`: copies the whole paragraph

## Put (Paste)

- Paste text in the current selection
- Text to be pasted must in vim's register
- vim does not have the ability from paste from you system clipboard

- `p`: paste below the current line
- `P`: paste above the current line

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

## Splitting

- `<C-w>v`: Split window vertically
- `<C-w>s`: Split window horizontally
- `<C-w>=`: Make splits equal size
