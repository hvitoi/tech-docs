# mkswap

- Swap space is used when the RAM memory is full
- Swap is localted in the local hard drive and therefore it's slow

## Create swap file

```shell
# Create swap file
# Swap file cannot be created via touch command because this way it would be an empty file
dd \
  if="/dev/zero" \ # Read from file (instead of standard input)
  of="/swapfile" \ # Write to a file (instead of standard output)
  bs="1M" \
  count="4G" # Total size of the file 4194304 = 4096M = 4G
  status="progress"

# Remove rwx permissions from other users
chmod 600 "/swapfile"

# Make swap out of the swap file
mkswap "/swapfile"

# Activate swap
swapon "/swapfile"
```

```shell
# Append new swap item to fstab (only if created after the genfstab command)
echo "/swapfile none swap sw 0 0" | tee -a "/etc/fstab`"
```

## Create swap from a partition

```shell
# Display all partition on the drive
fdisk -l

# Create swap partition via fdisk interative shell
fdisk "/dev/sdx"

# Make the swap
mkswap "/dev/sdc"

# Activate swap
swapon "/dev/sdc"
```

```shell
# Add the swap partition to the fstab
vim "/etc/fstab"
```
