# zpool

## status

- Test zfs installationd

## list

```shell
zpool list
```

```shell
# all pools
zpool status

# specific pool
zpool status -L <pool>
```

## create

- Create a `storage pool`

```shell
sudo zpool create \
  -f \
  -o ashift=12 \
  -O casesensitivity=insensitive \
  -O normalization=formD \
  -O compression=lz4 \
  -O atime=off \
  <pool> <vdev> <device-id1> <device-id2> <device-id3>
```

- `-f`: Force creating the pool. This is to overcome the "EFI label error".
- `-m`: mount point
  - `/<pool>` by default on Linux
  - `/Volume/<pool>` by default on macOS
- `-d`: disable all feature flags
- `-o`: Properties
- `-O`: File System Properties
- `<pool>`: arbitrary name for a pool
- `<vdev>`: type of the virtual device. E.g., raidz, mirror, etc
  - `mirror`: requires at least 2 devices
  - `raidz1`:
- `<device-id>`: disk identifier
  - If an entire disk is used (e.g., /dev/sda), a GPT table is automatically created

## set

- Set properties

```shell
# Compression
zfs set compression=lz4 <pool>
zfs set compression=on <pool>
```

## export

- It's the equivalent of unmounting a device before unplugging

```shell
zpool export <pool>

# force if there are open applications using data
zpool export -f <pool>
```

## import

- Scans the specified `path` and assemble an specified `pool name`
- Optionally pass an additional parameter to rename the existing pool

```shell
# by-id
zpool import -d /var/run/disk/by-id <pool>

# by-serial
zpool import -d /var/run/disk/by-serial <pool>

# by-path
zpool import -d /var/run/disk/by-path <pool>

# by-image-path
zpool import -d /var/run/disk/by-image-path <pool>

# by device name (not recommended as they vary)
sudo zpool import -d /dev <pool>
```

## destroy

- Destroy any data and remove all metadata on a mounted storage pool

```shell
zpool destroy <pool>
zpool destroy <pool>/<dataset>
```

## add

- Extends an existing pool

```shell
zpool add <pool> <device-id>
```

## scrub

- Verifies the integrity of a pool

```shell
zpool scrub <pool>
```
