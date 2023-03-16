# vulkaninfo

- `/usr/share/vulkan/icd.d/` shows the vulkan implementations installed on your system. E.g.

  - `intel_hasvk_icd.x86_64.json`: vulkan-intel
  - `intel_hasvk_icd.i686.json`: lib32-vulkan-intel

  - `intel_icd.x86_64.json`: vulkan-intel
  - `intel_icd.i686.json`: lib32-vulkan-intel

  - `radeon_icd.x86_64.json`: vulkan-radeon (RADV - part of mesa project)
  - `radeon_icd.i686.json`: lib32-vulkan-radeon (RADV - part of mesa project)

  - `amd_icd64.json`: amdvlk
  - `amd_icd32.json`: lib32-amdvlk

```shell
vulkaninfo
vulkaninfo | grep '^GPU id'

vulkaninfo --summary
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
