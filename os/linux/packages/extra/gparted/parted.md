# gparted

```shell
# interactive mode
parted "/dev/sda"

# list partition layout for all devices
parted -l
```

## print

```shell
# print partition table and partition numbers
parted "/dev/sda" print
```

## resizepart

```shell
# resize a partition
parted "/dev/sda" resizepart
```
