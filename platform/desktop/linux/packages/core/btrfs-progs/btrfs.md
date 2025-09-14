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

# default subvolume
btrfs subvolume get-default "."

# set the default volume (to be mounted without specifying subvol or subvolid)
btrfs subvolume set-default "/mnt"
```

## check

- Only use it if the filesystem cannot be mounted or is behaving very badly.

```shell
# read-only (do not attempt to fix)
btrfs check /dev/sdX
```

## scrub

- Checks for errors
- Works on a mounted filesystem, not directly on a block device.

```shell
btrfs scrub start -Bd /mnt
btrfs scrub status /mnt
```

## rescue

```shell
# Clear the tree log. Usable if it's corrupted and prevents mount
btrfs rescue zero-log "/dev/mapper/a"
```
