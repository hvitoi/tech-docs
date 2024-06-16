# copy

- It is always the contents of the directory that is synced, not the directory so when source:path is a directory, it's the contents of source:path that are copied, not the directory name and contents.

```shell
# Copy the content
rclone copy "/local/path" "remote":"/remote/path"
rclone copy ~/Documents/my-folder hvitoi:/my-folder
```
