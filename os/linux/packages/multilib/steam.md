# steam

## Proton

- Creates for each game a lightweight windows filesystem
- Translates the game into linux instructions
- Contains
  - `wine`: windows compatibility layer
  - `dxvk`: Direct X (9|10|11) to Vulkan translation
  - `dkd3d`: Direct X 12 to Vulkan translation
- Forks
  - `ge-proton`: allows more gaming support (aur: proton-ge-custom-bin)

## Custom proton install

- Grab the tarball from the provider website (e.g., `GE-Proton7-37.tar.gz`)
- Copy it into `~/.steam/compatibilitytools.d/`

## Launch parameters

```conf
DXVK_HUD=1 # fps counter
VKD3D_HUD=1 # fps counter
DXVK_FILTER_DEVICE_NAME=NAVI23 # force a gpu for Direct X (9|10|11) -- get the id from vulkaninfo | grep '^GPU id'
VKD3D_FILTER_DEVICE_NAME=NAVI23 # force a gpu for Direct X 12 -- get the id from vulkaninfo | grep '^GPU id'
__NV_PRIME_RENDER_OFFLOAD=1
__GLX_VENDOR_LIBRARY_NAME=nvidia
__NV_PRIME_RENDER_OFFLOAD=1
%command%
```
