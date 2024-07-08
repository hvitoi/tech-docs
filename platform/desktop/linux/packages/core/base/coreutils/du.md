# du

```shell
# Size of each folder inside the current folder
du
du "/directory"

# size of the items (files and folders in depth 1)
du -d1

# Size of each folder and individual files
du -a

# Human readable
du -h

# Show total size
du -s
du -sh
du -sh "/var/lib/docker" # docker image folder
du -sh *
```

## File size

```shell
echo -n "0123456789" > a.txt # 10-byte size file

# real size (filesystem size)
du --block-size=1 "a.txt" # 4096 bytes (the block size)

# apparent size
du --apparent-size --block-size=1 "a.txt" # 10 bytes

# apparent size (ls always show apparent)
ls -la # 10 bytes
```
