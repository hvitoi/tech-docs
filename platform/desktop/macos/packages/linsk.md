# linsk

- <https://github.com/AlexSSD7/linsk>

```shell
# manual
mv linsk_darwin_arm64_v0.2.2 /usr/local/bin/linsk

# go
go install "github.com/AlexSSD7/linsk@master"
```

## build

- Spin up a Linux VM

```shell
linsk clean # removes any previous VM
linsk build
```

## shell

- SSH into the VM with the drive passthrough

```shell
linsk shell dev:/dev/diskXsY --vm-mem-alloc 2048
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
sudo linsk run dev:/dev/diskXsY vdb --luks
```

- Open the storage network server (Cmd+K on Finder): `afp://linsk:<pass>@localhost:9000/linsk`
- By opening it, you are automatically mounting it to `/Volumes/linsk`
- You can also manually mount it `sudo mount_afp "afp://user:password@hostname/ShareName" /Volumes/ShareName`
