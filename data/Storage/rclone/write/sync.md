# Sync

```shell
# dry-run
rclone sync --dry-run /local/path remote:/remote/path # "test" the sync, but do not perform data transfer

# interactive mode
rclone sync -i /local/path remote:/remote/path # prompt for decisions

# progress mode
rclone sync -P /local/path remote:/remote/path # real-time transfer statistics

# verbose
rclone sync -v /local/path remote:/remote/path # show transferred files

# bandwidth
rclone sync -v /local/path remote:/remote/path --bwlimit 1.5M

# filters
rclone sync "/local/path" "remote":"/remote/path" --exclude "node_modules/"
```

```shell
# preferred
rclone sync \
  "/local/folder" \
  "remote:/remote/folder" \
  --verbose \
  --progress \
  --track-renames \
  --exclude "node_modules/" \
  --exclude "target/"
```
