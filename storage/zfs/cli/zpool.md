# zpool

## status

- Test zfs installationd

```shell
zpool status
```

## list

```shell
zpool list
```

## export

```shell
zpool export <pool-name>
```

## create

- Create a `storage pool`

```shell
sudo zpool create \
  -f \
  -o ashift=12 \
  -O casesensitivity=insensitive \
  -O normalization=formD \
  <pool> <vdev> diskX diskY diskZ
```

- `-f`: Force creating the pool. This is to overcome the "EFI label error".
- `-m`: mount point (`/<pool-name>` by default)
- `-o`: Properties
- `-O`: File System Properties
- `<pool>`: arbitrary name for a pool
- `<vdev>`: type of the virtual device. E.g., raidz, mirror, etc
- `<disk...>`: disk identifier
