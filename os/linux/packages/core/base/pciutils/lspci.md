# lspci

- Show PCI devices

```shell
lspci
lspci -k # Show PCI device alongside with its firmware
lspci -vvv # max verbose (run with sudo for more details)
lspci -mm # Readable
lspci -nn | grep VGA # get vid and pid
lspci -d ::0300 && lspci -d ::0302
```

## VGA controller

- Controller ending with `[VGA controller]` means is the active GPU (the others are switched off)

```shell
lspci -vk | grep -A 2 -E "(VGA|3D)"
```
