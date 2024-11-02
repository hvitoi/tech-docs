# fzf

```shell
# simple select
options=("Option 1" "Option 2" "Option 3")
selected=$(printf "%s\n" "${options[@]}" | fzf)
echo "You selected: $selected"
```

```shell
# Search in the arch repositories and preview/install the selected package
pacman -Slq | fzf --multi --preview 'pacman -Si {1}' | xargs -ro sudo pacman -S
```

## Fish integration

### Pacman

- Fish keybinding are installed at `/usr/share/fish/vendor_functions.d/fzf_key_bindings.fish`

```fish
# ~/.config/fish/functions/fish_user_key_bindings.fish
function fish_user_key_bindings
    fzf_key_bindings # enable key binding
end
```

### Homebrew

- On Homebrew the key bindings are not automatically added to vendor_functions.d. It must be done manually

```shell
mkdir $__fish_user_data_dir/vendor_functions.d
ln -sf $(brew --prefix)/opt/fzf/shell/key-bindings.fish $__fish_user_data_dir/vendor_functions.d/key-bindings.fish
```

- Or simply source it in the config

```shell
source $(brew --prefix fzf)/shell/key-bindings.fish
```
