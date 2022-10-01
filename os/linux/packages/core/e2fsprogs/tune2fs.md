# tune2fs

- Remove reserved space
- Reserved space can be removed from ext4 filesystems if you don't plan to install the system there

```shell
tune2fs -m 0 "/dev/sdx1"
```
