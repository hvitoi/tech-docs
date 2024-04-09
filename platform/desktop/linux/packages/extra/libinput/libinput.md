# libinput

- List event devices `/dev/input/event*`

## list-devices

```shell
libinput list-devices
```

## measure

- Requires `libinput-utils`

```shell
# Get the Kernel specified touchpad size
libinput measure touchpad-size 100x100 # 1x speed

# Multiply the kernel-specified size by a multiplier (1.5x, 0.8x, etc)
libinput measure touchpad-size 127.28x78.72 # 0.8x speed

```

159.1x98.4mm
