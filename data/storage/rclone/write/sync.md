# rclone sync

- Changes the destination only

```shell
# dry-run
rclone sync /local/path remote:/remote/path --dry-run

# interactive mode (prompt for decisions)
rclone sync /local/path remote:/remote/path --interactive

# verbose (show transferred files)
rclone sync /local/path remote:/remote/path --verbose

# real-time transfer statistics
rclone sync /local/path remote:/remote/path --progress

# bandwidth
rclone sync /local/path remote:/remote/path --bwlimit 1.5M

# filters
rclone sync "/local/path" "remote":"/remote/path" --exclude "node_modules/"
```

```shell
rclone sync \
  /local/folder \
  remote:/remote/folder \
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

### Copy (new)

```json
// dry-run
{
  "time":"2025-09-21T23:32:20.097645-03:00",
  "level":"notice",
  "msg":"Skipped copy as --dry-run is set (size 0)",
  "skipped":"copy",
  "size":0,
  "object":"foo/a.txt",
  "objectType":"*local.Object",
  "source":"slog/logger.go:256"
}

// run
{
  "time":"2025-09-21T23:42:18.863965-03:00",
  "level":"info",
  "msg":"Copied (new)",
  "size":14,
  "object":"foo/a.txt",
  "objectType":"*local.Object",
  "source":"slog/logger.go:256"
}
```

### Copy (overwrite)

```json
// dry-run (same as copy new)
{
  "time":"2025-09-21T23:50:36.640844-03:00",
  "level":"notice",
  "msg":"Skipped copy as --dry-run is set (size 13)",
  "skipped":"copy",
  "size":13,
  "object":"foo/a.txt",
  "objectType":"*local.Object",
  "source":"slog/logger.go:256"
}

// run
{
  "time":"2025-09-21T23:51:41.252991-03:00",
  "level":"info",
  "msg":"Copied (replaced existing)",
  "size":13,
  "object":"foo/a.txt",
  "objectType":"*local.Object",
  "source":"slog/logger.go:256"
}
```

### Delete

```json
// dry-run
{
  "time":"2025-09-21T23:38:23.239318-03:00",
  "level":"notice",
  "msg":"Skipped delete as --dry-run is set (size 0)",
  "skipped":"delete",
  "size":0,
  "object":"foo/a.txt",
  "objectType":"*crypt.Object",
  "source":"slog/logger.go:256"
}

// run
{
  "time":"2025-09-21T23:42:19.581362-03:00",
  "level":"info",
  "msg":"Deleted",
  "object":"foo/a.txt",
  "objectType":"*crypt.Object",
  "source":"slog/logger.go:256"
}
```

### Move

```json
// dry-run
{
  "time":"2025-09-21T23:32:20.432851-03:00",
  "level":"notice",
  "msg":"Skipped move to foo/b.txt as --dry-run is set (size 6)",
  "skipped":"move to foo/b.txt",
  "size":6,
  "object":"foo/a.txt",
  "objectType":"*crypt.Object",
  "source":"slog/logger.go:256"
}

// run
{
  "time":"2025-09-21T23:42:17.84027-03:00",
  "level":"info",
  "msg":"Moved (server-side) to: foo/b.txt",
  "object":"foo/a.txt",
  "objectType":"*crypt.Object",
  "source":"slog/logger.go:256"
}
```

```json
// dry-run & run
{
  "time":"2025-09-21T23:38:23.239236-03:00",
  "level":"info",
  "msg":"Renamed from \"foo/a.txt\"",
  "object":"foo/b.txt",
  "objectType":"*local.Object",
  "source":"slog/logger.go:256"
}
```

### Directory

- `Skipped set directory modification time as --dry-run is set`
- `Set directory modification time (using DirSetModTime)`
