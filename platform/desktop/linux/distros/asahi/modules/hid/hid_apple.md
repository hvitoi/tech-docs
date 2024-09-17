# hid-apple

- Keyboard layout

- **fnmode**
  - Mode of fn key on Apple keyboards
  - `0` = disabled
  - `1` = fkeyslast
  - `2` = fkeysfirst
  - `3` (default) = auto
- **iso_layout**
  - Swap the backtick/tilde and greater-than/less-than keys
  - `-1` (default) = auto
  - `0` = disabled
  - `1` = enabled
- **swap_opt_cmd**
  - Swap the Option ("Alt") and Command ("Flag") keys
  - `0` (default) = as-is, Mac layout
  - `1` = swapped, Windows layout
  - `2` = swapped, Swap only left side
- **swap_ctrl_cmd**
  - Swap the Control ("Ctrl") and Command ("Flag") keys
  - `0` (default) = No change
  - `1` = Swapped
- **swap_fn_leftctrl**
  - Swap the Fn and left Control keys
  - `0` (default) = as-is, Mac layout
  - `1` = swapped, PC layout

```conf
# /etc/modprobe.d/hid-apple.conf
options hid_apple swap_opt_cmd=1 swap_fn_leftctrl=1
```
