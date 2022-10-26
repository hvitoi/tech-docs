# all-ways-egpu-git

- Switch gpus on wayland

```sh
# Setup
all-ways-egpu
```

## boot

- Boot the GPU daemon
- The daemon is used to disable a particular gpu at startup
- Runs before the display manager

```sh
all-ways-egpu boot
```

## set-boot-vga

- Automatically set the `boot-vga` flag at startup
- Runs after the display manager

```sh
# set the eGPU as primary before the DE starts
all-ways-egpu set-boot-vga egpu

# set the iGPU as primary
all-ways-egpu set-boot-vga internal
```

## switch

- Enables a gpu

```sh
all-ways-egpu switch internal
```
