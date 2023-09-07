# fzf

```shell
# Search in the arch repositories and preview/install the selected package
pacman -Slq | fzf --multi --preview 'pacman -Si {1}' | xargs -ro sudo pacman -S
```

## Fish integration

- Fish keybinding are installed at `/usr/share/fish/vendor_functions.d/fzf_key_bindings.fish`

```fish
# ~/.config/fish/functions/fish_user_key_bindings.fish
function fish_user_key_bindings
    fzf_key_bindings # enable key binding
end
```
