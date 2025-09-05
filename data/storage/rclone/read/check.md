# rclone check

```shell
rclone check /local/dir remote:dir
rclone check /local/dir remote:dir --one-way

# list differences (detailed output)
# This will show the files which are missing or different
rclone check /local/dir remote:dir --verbose
```
