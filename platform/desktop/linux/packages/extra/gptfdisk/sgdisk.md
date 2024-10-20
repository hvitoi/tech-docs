# sgdisk

- Scripting version of gdisk

```shell
# print partition table (linux fs is typically 8300 code)
sgdisk /dev/disk0 -p

# Create partition to fill up the free space
sgdisk /dev/disk0 -n 0:0 -s
```
