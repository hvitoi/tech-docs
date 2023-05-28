# losetup

- Create a loop device based on an image

```shell
# mount
losetup -P loop50 "Monterey-recovery.dmg"
mount "/dev/loop50p2" mnt

# umount
umount mnt
losetup -d "/dev/loop50"
```
