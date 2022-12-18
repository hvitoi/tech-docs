# vulkaninfo

- `/usr/share/vulkan/icd.d/` shows the vulkan implementations installed on your system. E.g.
  - `intel_hasvk_icd.i686.json`: lib32-vulkan-intel
  - `intel_icd.i686.json`: lib32-vulkan-intel
  - `intel_hasvk_icd.x86_64.json`: vulkan-intel
  - `intel_icd.x86_64.json`: vulkan-intel
  - `radeon_icd.i686.json`: lib32-vulkan-radeon (RADV - part of mesa project)
  - `radeon_icd.x86_64.json`: vulkan-radeon (RADV - part of mesa project)

```shell
vulkaninfo
vulkaninfo | grep '^GPU id'

vulkaninfo --summary
```
