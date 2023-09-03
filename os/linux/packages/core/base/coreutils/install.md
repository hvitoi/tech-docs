# install

- Install a file/directory
- Works similarly to `cp` but with additional options

```shell
# copy a file
install /source/file /dest/dir
install skaffold /usr/local/bin/

# copy multiple files
install /source/dir/* -t /dest/dir

# copy a file (destination is treated as the filename)
install /source/file /dest/file -T

# copy creating missing directories as needed
install -D /source/file /dest/nested/dir

# copy and set the target permissions
install -m644 /source/file /dest/dir
install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
```
