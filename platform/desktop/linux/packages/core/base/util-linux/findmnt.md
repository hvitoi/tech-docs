# findmnt

- List all mounted filesystems

```shell
# all mounted filesystem in any device
findmnt

# ... in a specific device
findmnt /dev/sda1
findmnt -n -o TARGET /dev/nvme0n1p1

# ... in a specific location
findmnt /usr
```
