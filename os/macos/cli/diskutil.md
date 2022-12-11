# diskutil

## list

```shell
# list disks
diskutil list
```

## info

```shell
# info about a physical disk
diskutil info "/dev/disk0"
```

## mount

```shell
# mount a parition into /Volumes (EFI partition)
diskutil mount "disk0s1"
```

## unmount

```shell
# unmount partition
diskutil unmount "disk0s1"
```

## unmountDisk

```shell
diskutil unmountDisk "disk0"
```

## eject

```shell
diskutil eject "/dev/diskX"
```
