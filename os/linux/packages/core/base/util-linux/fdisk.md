# fdisk

- Modify partitions
- Show disk and devices (partitions)
- Requires sudo

```shell
# Show disks and devices
fdisk -l

# Pick a disk to modify
fdisk "disk"
fdisk "/dev/sdx"
  - `m`: Menu
  - `p`: print partitions
  - `n`: Add new partition # p for primary
  - `t`: Change partition system id
  - `w`: write/apply changes
```

## n

- `+10G` to set the size

## t

- `1`: EFI System
- `19`: Linux Swap
- `20`: Linux Filesystem
