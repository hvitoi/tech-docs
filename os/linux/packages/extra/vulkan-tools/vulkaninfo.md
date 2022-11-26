# vulkaninfo

- `/usr/share/vulkan/icd.d/` shows the vulkan implementations installed on your system. E.g.
  - `intel_icd.x86_64.json`: vulkan-intel
  - `radeon_icd.i686.json`: vulkan-radeon (RADV - part of mesa project)
  - `radeon_icd.x86_64.json`

```sh
vulkaninfo
vulkaninfo | grep '^GPU id'

vulkaninfo --summary
```
