# linsk

## build

- Spin up a Linux VM

```shell
linsk build
```

## ls

- Start the VM. passthrough a storage device and run `lsblk` in it
  - Pass the whole device through! Not only the partition
- It exits immediately

- The storage device on the VM is usually `/dev/vdb1`

```shell
sudo linsk ls dev:/dev/diskX
```

## run

- Actually mount the passed through volume in the VM and mount it

```shell
# Without encryption
sudo linsk run dev:/dev/diskX vdb1

# With luks encryption
sudo linsk run dev:/dev/diskX vdb1 -l
```

- On MacOS the storage network server is exposed at `afp://127.0.0.1:9000/linsk`
  - Cmd + K on Finder to open a network storage device
