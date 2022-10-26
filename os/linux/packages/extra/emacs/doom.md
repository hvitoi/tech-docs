# doom

- Doom Emacs is a framework on top of emacs
- <https://github.com/doomemacs/doomemacs>
- It install various packages from the emacs package manager
- The doom CLI must be added to the path `export PATH=$PATH:$HOME/.emacs.d/bin`
- `M-x` (Alt + x): execute any command

## sync

- Sync the config from doom with emacs
- After that you can launch doom from emacs directly

```sh
doom sync
```

## Configuration

- `~/doom.d/init.el`: internal packages
- `~/doom.d/packages.el`: 3rd party packages
- `~/doom.d/config.el`:

## Undo

- `C-_`: undo a previous change

## Directories

- `C-x d`: **dired** (file manager)

## Window Management

- `C-w v`: open a split on the cross-axis (vertically)
- `C-w h`: open a split on the main-axis (horizontally)

- `C-w c`: close a split screen (still open in background)
- `C-w w`: switch between splits

## Edit File

- `SPC .`: **find-file** (edit a file)

## Files

- `SPC f r`: find recent files

## Buffer

- The _fallback buffer_ is the main screen

- `SPC b k`: kills a window buffer
- `SPC b p`: go to the previous buffer
- `SPC b n`: go to the next buffer
- `SPC b i`: **ibuffer** (show all buffers opened)

## Host

- `SPC h r r`: restart doom emacs
- `SPC h i`: documentation browser

## Splitting

- `SPC w v`: vertical split
- `SPC w s`: horizontal split
- `SPC w c`: close split
- `SPC w w`: switch split
