# anylinuxfs

- <https://github.com/nohajc/anylinuxfs>

```shell
brew tap nohajc/anylinuxfs
brew install anylinuxfs
```

## list

- Show available linux filesystems

```shell
anylinuxfs list
```

## mount

- It must always refer to one or more partitions or logical volumes (not whole disks)

```shell
anylinuxfs mount /dev/diskXsY # rw
anylinuxfs /dev/diskXsY # same
anylinuxfs /dev/diskXsY -o ro
```

## shell

```shell
anylinuxfs shell /dev/diskXsY
```

## status

- Show what is currently mounted

```shell
anylinuxfs status
```

## stop

- Try to stop anylinuxfs in case umount or eject didn't completely terminate the VM

```shell
anylinuxfs stop
```

## config

```shell
# set memory requirement
anylinuxfs config -r 2560 # MiB
```

## log

```shell
anylinuxfs log
```
