# mkfs.fat

```shell
# FAT 32 partition
mkfs.fat -F32 "/dev/sdx1"

# With label
mkfs.fat "/dev/vda1" -F 32 -n "my-boot"
```
