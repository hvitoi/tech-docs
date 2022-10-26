# xargs

```sh
xargs -I "{}" echo Blah {} blabla {} < <(seq 1 5)
xargs -I "{}" code --install-extension {} --force < "$HOME/.dotfiles/vscode/extensions"
```
