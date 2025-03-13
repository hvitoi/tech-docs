# linsk

- <https://github.com/AlexSSD7/linsk>

```shell
mv linsk_darwin_arm64_v0.2.2 /usr/local/bin/linsk
```

## build

- Spin up a Linux VM

```shell
linsk build
```

## ls

- Start the VM, pass a storage device through, run `lsblk` on it & exits
- Pass only the desired partition (not the whole device, because it's not necessary)
- The storage device on the VM is usually `/dev/vdb`

```shell
sudo linsk ls dev:/dev/diskXsY
```

## run

- Actually mount the passed through volume in the VM and mount it

```shell
# Without encryption
sudo linsk run dev:/dev/diskXsY vdb

# With luks encryption
sudo linsk run dev:/dev/diskXsY vdb -l
```

- On MacOS the storage network server is exposed at `afp://127.0.0.1:9000/linsk`
- `Cmd + K` on Finder to open a network storage device
