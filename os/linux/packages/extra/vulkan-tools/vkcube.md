# vkcube

```shell
vkcube
```

## MESA_VK_DEVICE_SELECT

```shell
# list devices
MESA_VK_DEVICE_SELECT=list vkcube

# select a device to run (pick it from vendorID:deviceID from vulkaninfo --summary)
MESA_VK_DEVICE_SELECT=1002:73ff vkcube
MESA_VK_DEVICE_SELECT_FORCE_DEFAULT_DEVICE=1 vkcube
```

## MESA_VK_DEVICE_SELECT_FORCE_DEFAULT_DEVICE

```shell
# force run on the default device (device 0)
MESA_VK_DEVICE_SELECT_FORCE_DEFAULT_DEVICE=1 vkcube

```

## VK_LOADER_DEBUG

```shell
VK_LOADER_DEBUG=info vkcube
```

## VK_ICD_FILENAMES

- Set the preferred vulkan driver

```shell
VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/radeon_icd.x86_64.json vkcube
```
