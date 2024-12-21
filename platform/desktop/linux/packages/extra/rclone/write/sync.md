# rclone sync

- Changes the destination only

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
  --exclude "target/" \
  --exclude ".DS_Store" \
  --exclude ".localized"
```

## Log Level

DEBUG > INFO > NOTICE > ERROR

```shell
rclone sync foo remote:foo --log-level NOTICE
```

```shell
# Shows files and its taken action
rclone sync foo remote:foo --combined - -P
```

## Log Formatting

```shell
rclone sync foo google-drive:foo --track-renames --verbose --use-json-log 2>&1 |
  jq -r '
          def colors:
            {
              "green": "\u001b[32m",
              "cyan": "\u001b[36m",
              "yellow": "\u001b[33m",
              "red": "\u001b[31m"
            };

          select(.objectType == "*local.Object" or (.objectType == "*drive.Object" and .msg == "Deleted"))
            | if (.msg | startswith("Copied (new)")) then colors.green + "U " + .object
              elif (.msg | startswith("Copied (replaced existing)")) then colors.cyan + "M " + .object
              elif (.msg | startswith("Renamed")) then colors.yellow + "R " + .object
              elif (.msg | startswith("Deleted")) then colors.red + "D " + .object
              else null end
        '
```
