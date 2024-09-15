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

- Mount a partition/volume into `/Volumes`
- The volume must be decrypted already (otherwise use diskutil apfs)

```shell
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

## listFilesystems

```shell
diskutil listFilesystems
```

## eraseDisk

```shell
diskutil eraseDisk %noformat% /dev/disk0s0
```

## eraseVolume

- Erases a disk and format it with a new filesystem
- Uses the command `newfs_*` under the hood (e.g., `newfs_apfs`)
- List the formattable file systems with `diskutil listFilesystems`

```shell
# APFS
diskutil eraseVolume "APFS" "Untitled" "diskXsY"

# Unallocated space
diskutil eraseVolume free free disk0s5
```

## apfs

### list\*

```shell
diskutil apfs list
```

### deleteVolume

```shell
diskutil apfs deleteVolume disk0s0
```

### deleteContainer

- Completely remove an APFS container making it `free space`

```shell
diskutil apfs deleteContainer disk0s0
```

### unlockVolume

- Unlock and mount a volume
- It searches for all passwords for all cryptographic users

```shell
diskutil apfs unlockVolume disk1s1
```

### listCryptoUsers | listUsers | listCryptoKeys | listKeys

- List keys/users associated with a given volume

```shell
diskutil apfs listCryptoUsers disk1s1
```

### listSnapshots

- List snapshots associated with a volume
- A snapshot reference may also be used (3-part BSD identifier, e.g., disk1s2s1)

```shell
diskutil apfs listSnapshots disk1s1
diskutil apfs listSnapshots disk1s4s1
```

### listVolumeGroups

- List volume groups in a given container
- Usually encapsulates System + Data

```shell
diskutil apfs listVolumeGroups disk1
```
