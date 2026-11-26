# make

- Utility to manage programs
- It's a `universal packager` for linux distributions (or basically anything)
- In archlinux it's more common to use `PKGBUILD`

```shell
make # "all" script
make "install" # "install" script
make "uninstall" # "uninstall" script

# Suppress echoing the command (even if the command doesn't start with @)
make -s
make install my_arg=hii # provide arguments. Can be accessed with $(my_arg) inside of the Makefile
```
