# copy

- When `source` is a directly, the content of the directory are copy (not the directory itself)
- If `dest` does not exist, it is then created

```shell
# Copy directory content
rclone copy "/local/path" "remote:/remote/path"

# Copy file
rclone copy "/local/path/file.txt" "remote:/remote/path"
```
