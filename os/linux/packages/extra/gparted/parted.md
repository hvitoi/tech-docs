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

## mklabel

```shell
# GPT
parted "/dev/sda" -- mklabel "gpt"

# MSDOS (MBR)
parted "/dev/sda" -- mklabel "msdos"
```

## mkpart

```shell
# root partition
parted "/dev/sda" \
  -- \
  mkpart primary 512MB -8GB

# swap partition
parted "/dev/sda" \
  -- \
  mkpart primary linux-swap -8GB 100%

# boot partition
parted "/dev/sda"
  \ -- \
  mkpart ESP fat32 1MB 512MB

parted "/dev/sda" \
  -- \
  set 3 esp on
```

## set

```shell
# set partition 1 as the boot partition
parted "/dev/sda" \
  -- \
  set 1 boot on

# set partition 3 as the esp partition
parted "/dev/sda" \
  -- \
  set 3 esp on
```
