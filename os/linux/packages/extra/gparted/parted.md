# gparted

```sh
# interactive mode
parted "/dev/sda"

# list partition layout for all devices
parted -l
```

## print

```sh
# print partition table and partition numbers
parted "/dev/sda" print
```

## resizepart

```sh
# resize a partition
parted "/dev/sda" resizepart
```
