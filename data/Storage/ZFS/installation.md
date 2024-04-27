# Installation

## MacOS Install

- Enable `Custom Kernel Extensions` from macOS recovery
- Download the latest release from <https://github.com/openzfsonosx/openzfs-fork>
- Install the `.pkg`
- Verify that the extension is loaded with `kextstat`

## Linux Install (arch)

- Install the kernel module and the utils (`zfs-utils`)

```shell
yay -S zfs-dkms # install zfs-utils as dependency
```
