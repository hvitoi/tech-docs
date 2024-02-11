# zfs-utils

- Manage `zfs` filesystems
- The kernel module is installed with `zfs-dkms` (aur)
  - The module will be rebuilt on every kernel upgrade

## MacOS Install

- Enable `Custom Kernel Extensions` from macOS recovery
- Download the latest release from <https://github.com/openzfsonosx/openzfs-fork>
- Install the `.pkg`
- Verify that the extension is loaded with `kextstat`

## zpool

### status

- Test zfs installationd

```shell
zpool status
```

### list

```shell
zpool list
```

### export

```shell
zpool export
```
