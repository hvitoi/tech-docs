# fdisk

- Modify partitions
- Show disk and devices (partitions)
- Requires sudo

```shell
# Show disks and devices
fdisk -l

# Start fdisk on a disk
fdisk /dev/sdx

# start disk on a disk (and wipe existing signatures)
fdisk /dev/sdx --wipe auto

# Pick a disk to modify
fdisk "disk"
fdisk "/dev/sdx"
  - `m`: Menu
  - `p`: print partitions
  - `n`: Add new partition # p for primary
  - `t`: Change partition system id
  - `w`: write/apply changes
```

## g

- Creates a new empty `GPT partition table`
- GPT is the `disklabel type`
- This is usually the first step on a new drive

## n

- `+10G` to set the size

## t

- Partition types (alias) for GPT
  - `1`: EFI System
  - `19`: Linux Swap
  - `20`: Linux Filesystem
