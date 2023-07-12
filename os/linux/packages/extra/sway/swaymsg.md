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
```
