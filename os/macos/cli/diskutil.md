# diskutil

```shell
# list disks
diskutil list

# info about a physical disk
diskutil info "/dev/disk0"

# mount a parition into /Volumes (EFI partition)
diskutil mount disk0s1

# unmount partition
diskutil unmount disk0s1
```
