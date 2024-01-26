# chroot

- chroot into another filesystem
- The chrooted system do not need to have a kernel `/boot/vmlinuz-linux`
- No process files `/proc`

```shell
# Exec bash from the new fs
chroot "mynewroot/" "/bin/bash"

# Export path in the new fs
expor PATH=/sbin:/bin
```
