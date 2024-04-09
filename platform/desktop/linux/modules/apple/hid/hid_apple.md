# hid-apple

- Keyboard layout

```conf
# /etc/modprobe.d/hid-apple.conf

# swap_opt_cmd
# 0 = as silkscreened, Mac layout (Default)
# 1 = swapped, PC layout

# swap_fn_leftctrl
# 0 = as silkscreened, Mac layout (Default)
# 1 = swapped, PC layout

options hid_apple swap_opt_cmd=1 swap_fn_leftctrl=1
```
