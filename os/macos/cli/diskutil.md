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

## deleteVolume

```shell
diskutil apfs deleteVolume disk1s7
```

## apfs

### list\*

```shell
diskutil apfs list
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

- APFSCryptoUserType
  - `LocalOpenDirectory`: a local user
  - `PersonalRecovery`: recovery key generated at encryption time
  - `MDMRecovery`

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
