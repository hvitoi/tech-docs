# xargs

- Useful for piping command together but the commands do not accept piped input
- `xargs` can take the output from one command and send it to another command as parameters.
- `xargs` accepts piped input or file input and uses it to feed another command

```shell
# just echo it out as an array (even if the input is multiline)
ls -1 | xargs
ls -1 | xargs echo # same
```

```shell
mkdocs get-deps | xargs pip install
```

```shell
xargs -I "{}" echo 'I am {}!' <<< 'Henrique'
xargs -I "{}" echo Blah {} blabla {} < <(seq 1 5)
xargs -I "{}" code --install-extension {} --force < "$HOME/.dotfiles/vscode/extensions"
```

```shell
dmenu_path | dmenu | xargs swaymsg exec --
```
