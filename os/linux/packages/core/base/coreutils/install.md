# install

- Install a file/directory
- Works similarly to `cp` but with additional options

```shell
install /source/file /dest/dir
install skaffold /usr/local/bin/
```

```shell
# install all files in /source/dir into /target/dir
install /source/dir/* -t /dest/dir
```

```shell
# Destination is treated as the filename
install /source/file /dest/file -T
```

```shell
# create directories are created as needed
install /source/file /dest/nested/dir -D
```

```shell
# set the permission of the file to be copied to the destination directory
install /source/file /dest/dir -m644
```
