# rclone copy

- When `source` is a directory, the content of the directory is copied (not the directory itself)
- If `dest` does not exist, it is then created

```shell
# Copy directory content
rclone copy "/local/dir" "remote:dir"

# Copy file
rclone copy "/local/file" "remote:dir"
```
