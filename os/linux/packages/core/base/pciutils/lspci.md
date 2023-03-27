# lspci

- Show PCI devices

```shell
lspci

# Readable
lspci -mm # Readable format

# Verbose
lspci -vvv # run with sudo for more details

# Drivers
lspci -k # Show PCI device alongside with its firmware

# Textual & Numeric ID
lspci -nn # -n for numeric only

# Select device
lspci -d "vendor:device:class"
lspci -d "::0300" # GPU class
lspci -d "::0302" # GPU class (alternative)

lspci -d "1002::" # AMD vendor
lspci -d "1002:73ff:0300" # Specific GPU from AMD vendor
```

## VGA controller

- Controller ending with `[VGA controller]` means is the active GPU (the others are switched off)

```shell
lspci -vk | grep -A 2 -E "(VGA|3D)"
```

sudo lspci -v -d 1002:
