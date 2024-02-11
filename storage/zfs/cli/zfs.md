# zfs

## list

```shell
# List all datasets in all pools
zfs list
zfs list <pool>/<dataset> # specific dataset

# Additional space information
zfs list -o space

# Snapshots of a given dataset
zfs list -t snapshot <pool>/<dataset>
```

## create

- Creates a `dataset`
- It allows a more granularity on the management of a pool
- It's similar to a subvolume in BTRFS
- It appears as a folder in the zpool

```shell
zfs create <pool>/<dataset>

# set properties at creation
zfs create -o compression=gzip <pool>/<dataset>

# set encryption
zfs create -o encryption=on -o keylocation=prompt -o keyformat=passphrase <pool>/<dataset>
```

## destroy

- Destroys  a `dataset`
- The folder is removed (as well as its data)

```shell
zfs destroy <pool>/<dataset>
```

## clear

```shell
zpool clear <pool>
```

## get

- Get a property of a dataset

```shell
zfs get <property> <pool>/<dataset>
zfs get "compression" <pool>/<dataset>
zfs get "compressratio" <pool>/<dataset>
```

## set

- Set properties for a dataset

```shell
zfs set quota=20G <pool>/<dataset>
```

## load-key

- Load a key of a dataset in order to enable it to be mounted

```shell
zfs load-key <pool>/<dataset>

zfs mount <pool>/<dataset>
```

## mount

```shell

zfs mount <pool>/<dataset>
```

## snapshot

- Snapshot are created per dataset
- It's saved under `<dataset-root>/.zfs/snapshot/`

```shell
zfs snapshot <pool>/<dataset>@$(date +%Y-%m-%d-%H%M)
```
