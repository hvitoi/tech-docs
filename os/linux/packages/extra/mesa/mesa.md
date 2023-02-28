# mesa

- Provides `nouveau` drivers (open-source nvidia drivers)

## Environment variables

- <https://docs.mesa3d.org/envvars.html>

### Core Mesa

```shell
# Select a different GPU (other than the default)
# Applies to vulkan or OpenGL
DRI_PRIME=1

# pick it from vendorID:deviceID from vulkaninfo --summary or lspci -nn | grep VGA
DRI_PRIME=1002:73ff vkcube # AMD Radeon RX 6600 XT (RADV NAVI23)
DRI_PRIME=1002:7340 vkcube # AMD Radeon Graphics (RADV NAVI14)
DRI_PRIME=8086:3e9b vkcube # Intel(R) UHD Graphics 630 (CFL GT2)
```

## Vulkan mesa device select layer

- Requires `vulkan-mesa-layers`

```shell
# list devices
MESA_VK_DEVICE_SELECT=list vkcube

# select a device to run (pick it from vendorID:deviceID from vulkaninfo --summary)
MESA_VK_DEVICE_SELECT=1002:73ff vkcube
```

```shell
# force run on the default device (device 0)
MESA_VK_DEVICE_SELECT_FORCE_DEFAULT_DEVICE=1 vkcube
```

### RADV driver

```shell
RADV_PERFTEST=nosam # disable optimizations that get enabled when all VRAM is CPU visible.
RADV_PERFTEST=gpl # enable graphics pipeline library
```
