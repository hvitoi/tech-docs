# btrfs

## filesystem

```shell
btrfs filesystem usage "/"

btrfs filesystem df "/"

btrfs filesystem show "/"

# assign label to a btrfs filesystem
btrfs filesystem label /dev/mapper/lala LALA
```

## subvolume

- Subvolumes within a btrfs filesystem share the same UUID (same device!)
- That means that subvolumes share the same maximum device size
- The same device (with different subvolumes) is mounted into different mount points
- There is a convention to use prefix the subvolume name with `@` to indicate that it will be used as mount point. And `@` to the subvolume that will be mounted to root
- The top level subvolume is ID=5, subvol=/
- A size `quota` can be imposed for each subvolume
- Subvolumes can be referenced in fstab by name (e.g., `subvol=/@files` ) or by id (e.g., `subvolid=243`) mount flags

```shell
# List all subvolumes and snapshots in the filesystem
btrfs subvolume list "/"

# Create subvolume
btrfs subvolume create "/new-subvol"
mount "/dev/sda" "/home" -o subvol=/path/to/subvolume,subvolid=objectid

# take a snapshot of a subvolume (the snapshot itself is created as a new subvolume)
btrfs subvolume snapshot "/" "/my-snapshot"

# set the default volume (to be mounted without specifying subvol or subvolid)
btrfs subvolume set-default "/mnt"
```
