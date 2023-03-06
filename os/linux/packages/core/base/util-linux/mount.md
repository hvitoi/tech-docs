# mount

- Mount the volume to a folder

```shell
# list mount points in the order they were mounted
mount
mount -l
```

```shell
# mount
mount "device" "directory"
mount "/dev/sdx1" "/mnt"
mount "LABEL=FOO" "/mnt"
mount "UUID=1234..." "/mnt"

# create directories as necessary
mount "/dev/sda1" "/mnt/boot" --mkdir
mount "/dev/sda1" "/mnt/boot" -m

# mount by label
mount /mnt -L "FOO" # same as mount LABEL=FOO /mnt

# show mounts
mount -a

# mount with flag options
mount -o noatime,compress=zstd,ssd,discard=async,space_cache=v2,subvol=@ "/dev/vda2" "/mnt"
```

## Mount options

### Filesystem-independent options

- `man mount`

- **sync**: all i/o to the fs is done synchronously
- **async**: all i/o to the fs is done asynchronously

- **atime**: inode access time is controlled by kernel defaults
- **noatime**: do not update inode access times on this fs (for faster access)

- **auto**: this fs is mounted with the `-a` option
- **noauto**: not mounted automatically with `-a` option

- **dev**: interpret character or block special devices on the fs
- **nodev**: do not interpret character or block special devices

- **exec**: permit the execution of executable files in the fs
- **noexec**: do not permit the execution of executable files in the fs

- **user**: allow an ordinary user to mount the fs (if the user is in the mtab list)
- **owner**: allow an ordinary user to mount the fs (if the user is the owner of the device)
- **group**: allow an ordinary user to mount the fs (if one of the user's group match the group of the device)
- **users**: allow any ordinary user to mount the fs

- **nofail**: do not return error code if the device fails to mount

- _defaults_: `rw`, `suid`, `dev`, `exec`, `auto`, `nouser`, `async`

### btrfs options

- `man 5 btrfs`

- **compress=...**: `zlib`, `lzo`, `zstd`, `no`
- **discard=...**: Enable discarding of freed file blocks. `async` or `sync`
- **space_cache=...**: Options to control the free space cache. `v2`, `v1`
- **ssd**: Options to control SSD allocation schemes
- **subvol**: subvolume path
- **subvolid**: subvolume id

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
