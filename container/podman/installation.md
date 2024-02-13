# Installation

## macOS

- Podman on macOS uses `HVF` with `QEMU` to virtualize `Fedora CoreOS` (FCOS)

```shell
brew install podman

# Linux VM
podman system connection list # empty
podman machine init # new vm (fedora)
podman machine start # start vm

# Info
podman info
