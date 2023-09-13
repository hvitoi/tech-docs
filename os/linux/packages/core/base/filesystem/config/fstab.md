# /etc/fstab

- `/etc/fstab`
- `fstab` file can be used to define how disk partitions, various other block devices, or remote filesystems should be mounted into the filesystem
- These definitions will be converted into `systemd mount` units dynamically at boot

```conf
# <device>                                      <dir>                   <type>  <options>               <dump>  <fsck>

# /dev/sdb3 - arch
UUID=2740a3e6-85af-4d4a-bf60-242614758599       /                       ext4    rw,relatime             0       1

# /dev/sdc - swap
UUID=be520a04-5f31-46cb-a881-29a86a1133fe       none                    swap    defaults                0       0

# /dev/sda1 - moon
#UUID=4093109d-4077-422e-a87b-fb837e63de6f      /media/hvitoi/moon      ext4    defaults,noauto         0       2
```

## genfstab

- `genfstab` is a util to generate the fstab avaialble at the package `arch-install-scripts`

```shell
genfstab -U "/mnt" >> "/mnt/etc/fstab" # by UUID
genfstab -L "/mnt" >> "/mnt/etc/fstab" # by label
```

## Persistent Block Device Naming

- <https://wiki.archlinux.org/title/Persistent_block_device_naming>

- **PARTUUID**
  - Partition identifier
  - Available GPT disks
  - Can be set using `gdisk`
- **PARTLABEL**
  - Partition label
  - Available GPT disks
  - Can be set using `gdisk` (max 72 characters long)
  - Partition labels are defined in the header of the partition entry on GPT disks
- **UUID**
  - Filesystem identifier
  - Can be set with filesystem-specific tools (e.g., e2label, xfs_admin, fatlabel)
- **LABEL**
  - Filesystem label
  - Can be set with filesystem-specific tools (e.g., e2label, xfs_admin, fatlabel)
