# swaymsg

```shell
# Execute command
swaymsg -- output * resolution --custom 1920x1080

swaymsg focus output <name-or-identifier>
```

## IPC Message Types

### get_outputs

```shell
# Get monitor devices
swaymsg --type get_outputs
```

### get_inputs

```shell
# Get input devices
swaymsg --type get_inputs

# Get the layout of a keyboard
swaymsg -t get_inputs | jq -r '.[] | select(.identifier == "<kbd_identifier>") | .xkb_active_layout_name'
```

### get_tree

```shell
swaymsg --type get_tree

# app_id of the currectly focused window
swaymsg -t get_tree | jq -r '..|try select(.focused == true)'
```
