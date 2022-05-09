# vi

## Movement

- Movement commands can be added any number multiplier in front of it

- `h`: left
- `l`: right
- `k`: up
- `j`: down

- `^` / `0`: beggining of line
- `$`: end of line

- `w`: next word (first char)
- `b`: previous word (first char)

- `e`: next word (last char)

- `{`: next empty line
- `}`: previous empty line

- `%`: alternate between opening and closing characters. E.h., ( and ), [ and ]

- `gg`: top of the document
- `25%`: a quarter of the document
- `50%`: half of the document
- `G`: bottom of the document

- `''`: return to the previous position

- `Ctrl` + `g`: shows current position
- `Ctrl` + `u`: half page up
- `Ctrl` + `d`: half page down

## Insert

- `i`: Insert mode at left of current selection
- `I`: Insert mode at the beginning of line

- `a`: Insert mode at right of current selection
- `A`: Insert mode at the end of line

- `o`: Insert mode at a new line (after)
- `O`: Insert mode at a new line (before)

## Delete

- `d` can be combined with any other movement comand so that it will delete all the way through
- deleted text is regsitered in vim so that it can be pasted afterwards

- **Delete character**: `x`
- **Delete until end of line**: `D`
- **Delete whole line**: `dd`

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

## Yank

- `y` copies from a command or visual selection
- `yy`: yank the whole line
- `yap`: copies the whole paragraph

## Select

- `v` stands for _visual selection_
- `V`: selects the whole line
- `gg` -> `v` -> `G`: selects the whole document
- `vap`: visually selects around the paragraph

- `Ctrl+v`: block selection

## Put

- Put (or paste) text in the current selection
- Text to be pasted must in VIM's register
- VIM does not have the ability from paste from you system clipboard

- `p`

## Replace

- `r`: replace one letter
- `R`: replace mode (overwrite the text that's already there)

## Period

- `.`: executes the last command

## Undo / Redo

- **Undo last operation**: `u`
- **Undo whole line**: `U`

- **Redo**: `Ctrl` + `r`

## Focus

- **Focus the current line (middle)**: `z` + `z`
- **Focus the current line (top)**: `z` + `t`

## Quit

- **Save and Quit**: `Z` + `Z`
- **Quit without saving**: `Z` + `Q`

## Search

- `/keywordtobesearched`: search forwards
- `?keywordtobesearched`: search backwards
- `n`: next occurrence
- `N`: previous occurrence

## Commands

- `:w`: save file
- `:w!`: save file (force)
- `:w !sudo tee %`: save file with sudo

- `:q`: quit
- `:x`: save and quit

- `:!`: execute any shell command
- `:!ls`: execute any shell command
- `:!ps -ef`: execute any shell command

- `:sort`: sort the text selected

- `:earlier 5m`: go to the state 5 minutes before
- `:later 5m`: go to the state 5 minutes after

- `:s/old/new`: replace first occurrence (only applicable for the current line)
- `:s/old/new/c`: prompts the substitute or not
- `:s/old/new/g`: replace all occurrences within the line
- `:%s/old/new/g`: replace all occurrences throughout the document

- `:norm .`: executes period (last command) for all lines selected

- `:set hls`: set a variable called "hls" (highlight search)
- `:set ic`: set a variable called "ic" (ignore case)

- `:help`

- `:e ~/.vimrc`: start editing config file
