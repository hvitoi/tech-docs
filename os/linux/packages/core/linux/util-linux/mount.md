# mount

- Mount the volume to a folder

```shell
# mount
mount "partition" "folder"
mount "/dev/sdx1" "/data"
mount "/dev/sda1" "/mnt/boot" --mkdir # create folder

# show mounts
mount -a

# mount with options
mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@ "/dev/vda2" "/mnt"
```

## Permanent mount

- `/etc/fstab`

```conf
# <file system> <mount point> <type> <options> <dump> <pass>
UUID=bb3cfb59-f713-41db-8b1c-5fe4a217e27a / ext4 errors=remount-ro 0 1 # Debian
UUID=103C-FD10 /boot/efi vfat umask=0077 0 1 # EFI
#/media/hvitoi/Dummy/swapfile none swap sw 0 0 # Swap
UUID=cb63196a-d3d3-4d2d-b5da-41727f058dbc swap swap defaults 0 0 # Swap
UUID=C2D8DF53D8DF43F7 /media/hvitoi/Moon ntfs defaults,uid=1000 0 0 # Moon
```
