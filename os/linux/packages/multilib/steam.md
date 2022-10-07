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
