# Commands

## q

- `q`: quit

## w

- `:w`: save file
- `:w!`: save file (force)
- `:w !sudo tee %`: save file with sudo
- `:x`: save and quit

## s

- `:s/old/new`: replace first occurrence (only applicable for the current line)
- `:s/old/new/c`: prompts the substitute or not
- `:s/old/new/g`: replace all occurrences within the line
- `:%s/old/new/g`: replace all occurrences throughout the document

## r

- `:r !command`" paste output from a command

## e

- `:e ~/.vimrc`: start editing config file
- `:e ~/file.txt`: open a file

## \\

- `:!`: execute any shell command
- `:!ls`: execute any shell command
- `:!ps -ef`: execute any shell command

## sort

- `:sort`: sort the text selected

## earlier

- `:earlier 5m`: go to the state 5 minutes before

## later

- `:later 5m`: go to the state 5 minutes after

## norm

- `:norm .`: executes period (last command) for all lines selected

## set

- `:set hls`: set a variable called "hls" (highlight search)
- `:set ic`: set a variable called "ic" (ignore case)
- `:set paste`: allow paste from clipboard

## source

- Useful for loading new config right after changing it

- `:source %`

## healthcheck

- `:healthcheck`

## help

- `:help`
- `:help nvim`
- `:help news`
- `:help rtp`: runtimepath help

## close

```conf
# closes the current window
close
```

- `<cmd>close<CR>`: for keybindings

## Netrw

- Netrw is the default filetree explorer

```conf
Explore # open netrw in the directory of the currently opened file
```

- `%`: create new file
- `d`: create new directory

```conf
# tree-style explorer
let g:netrw_liststyle = 3
```
