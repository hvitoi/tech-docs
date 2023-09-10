# diskutil

## list

```shell
# list disks
diskutil list
```

## info

```shell
# info about a physical disk
diskutil info "/dev/diskX"
```

## mount

```shell
# mount a parition into /Volumes (EFI partition)
diskutil mount "diskX"
```

## unmount

```shell
# unmount partition
diskutil unmount "diskX"
```

## mountDisk

- Mount all volumes of a disk/partition

```shell
diskutil mountDisk "/dev/diskX"
```

## unmountDisk

- Unmount all volumes of a disk/partition

```shell
diskutil unmountDisk "/dev/diskX"
```

## eject

```shell
diskutil eject "/dev/diskX"
```
