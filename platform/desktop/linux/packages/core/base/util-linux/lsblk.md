# lsblk

- Show disks
- It's usually polluted due to snap packages (each pkg is a mounted fs)

```shell
lsblk
lsblk -f # output info about filesystems
lsblk -m # output info about permissions

# exclude loopback devices
lsblk -e 7

# select columns to display
lsblk -o "type,name,uuid,label"
```
