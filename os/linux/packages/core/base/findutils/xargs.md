# xargs

```shell
xargs -I "{}" echo 'I am {}!' <<< 'Henrique'
xargs -I "{}" echo Blah {} blabla {} < <(seq 1 5)
xargs -I "{}" code --install-extension {} --force < "$HOME/.dotfiles/vscode/extensions"
```

```shell
dmenu_path | dmenu | xargs swaymsg exec --
```
