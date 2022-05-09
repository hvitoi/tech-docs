# lspci

- Show PCI devices

```shell
lspci
lspci -k # Show PCI device alongside with its firmware
lspci -vvv # max verbose
lspci -mm # Readable
```

## VGA controller

- Controller ending with `[VGA controller]` means is the active GPU (the others are switched off)

```shell
lspci -vk | grep -A 2 -E "(VGA|3D)"
```
