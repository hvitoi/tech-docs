# vulkan-mesa-layers

- Offers multi-gpu support
- Allows selecting a gpu to run on

## MESA_VK_DEVICE_SELECT

```shell
# list devices
MESA_VK_DEVICE_SELECT=list vkcube

# select a device to run (pick it from vendorID:deviceID from vulkaninfo --summary)
MESA_VK_DEVICE_SELECT=1002:73ff vkcube
```

## MESA_VK_DEVICE_SELECT_FORCE_DEFAULT_DEVICE

```shell
# force run on the default device (device 0)
MESA_VK_DEVICE_SELECT_FORCE_DEFAULT_DEVICE=1 vkcube
```
