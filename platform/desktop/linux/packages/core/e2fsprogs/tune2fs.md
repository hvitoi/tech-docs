# tune2fs

- Remove reserved space
- Reserved space can be removed from ext4 filesystems if you don't plan to install the system there

```shell
tune2fs "/dev/sdx1" -m 0

# Filesystem information
tune2fs "/dev/sdx1" -l | grep "Block size"

# Set filesystem label
tune2fs -L "YOUR_LABEL" /dev/sdx1
```
