# vscode

## Configuration

```shell
# MacOS
ln -sF ~/.dotfiles/vscode/settings.json ~/Library/Application\ Support/Code/User/settings.json
ln -sF ~/.dotfiles/vscode/keybindings.json ~/Library/Application\ Support/Code/User/keybindings.json
ln -sF ~/.dotfiles/vscode/tasks.json ~/Library/Application\ Support/Code/User/tasks.json

# Linux
ln -sF ~/.dotfiles/vscode/settings.json ~/.config/Code/User/settings.json
ln -sF ~/.dotfiles/vscode/keybindings.json ~/.config/Code/User/keybindings.json
ln -sF ~/.dotfiles/vscode/tasks.json ~/.config/Code/User/tasks.json
```

## Extensions

```shell
code --list-extensions > ~/.dotfiles/vscode/extensions
xargs -n1 code --install-extension < ~/.dotfiles/vscode/extensions
```
