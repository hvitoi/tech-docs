# whiptail

- `Newt` is a library for TUI interfaces
- <https://en.wikipedia.org/wiki/Newt_(programming_library)>

```shell
selected=$(whiptail \
            --title "Choose an option" \
            --menu "Select an option" \
            15 60 4 \
            "1" "Option 1" \
            "2" "Option 2" \
            "3" "Option 3" 3>&1 1>&2 2>&3)

echo "You selected: $selected"
```
