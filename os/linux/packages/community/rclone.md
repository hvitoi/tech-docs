# rclone

## config

- Config file is stored at `~/.config/rclone/rclone.conf`

```shell
# Configure remote storage server
rclone config
rclone config file # print config file location
```

## listremotes

```shell
# Get all remotes
rclone listremotes

# Get storage info about a remote
rclone about "remote":"path"
rclone about hvitoi:/
```

## List

```shell
# Files
rclone lsf "remote":"path"

# Tree
rclone tree "remote":"path"

# Text-based UI
rclone ncdu "remote":"path"
```

## Copy

- It is always the contents of the directory that is synced, not the directory so when source:path is a directory, it's the contents of source:path that are copied, not the directory name and contents.

```shell
# Copy the content
rclone copy "/local/path" "remote":"/remote/path"
rclone copy ~/Documents/my-folder hvitoi:/my-folder
```

## Remove

```shell
# Remove a single file
rclone deletefile "remote":"remote/path"

# Remove a path and all of its contents
rclone purge "remote":"remote/path"
rclone purge "remote":"remote/path" --dry-run
rclone purge "remote":"remote/path" --interactive
```

## Sync

```shell
# dry-run
rclone sync --dry-run "/local/path" "remote":"/remote/path" # "test" the sync, but do not perform data transfer

# interactive mode
rclone sync -i "/local/path" "remote":"/remote/path" # prompt for decisions

# progress mode
rclone sync -P "/local/path" "remote":"/remote/path" # real-time transfer statistics

# verbose
rclone sync -v "/local/path" "remote":"/remote/path" # show transferred files

# bandwidth
rclone sync -v "/local/path" "remote":"/remote/path" --bwlimit 1.5M

# preferred
rclone sync \
  "/local/folder" \
  "remote:/remote/folder" \
  --verbose \
  --progress \
  --exclude "node_modules/"

rclone sync "/media/document" "remote:/document" --verbose --progress --exclude "node_modules/" --exclude "target/"
rclone sync "/media/image" "remote:/image" --verbose --progress --exclude "node_modules/" --exclude "target/"
rclone sync "/media/music" "remote:/music" --verbose --progress --exclude "node_modules/" --exclude "target/"
rclone sync "/media/video" "remote:/video" --verbose --progress --exclude "node_modules/" --exclude "target/"
rclone sync "/media/code" "remote:/code" --verbose --progress --exclude "node_modules/" --exclude "target/"
```

## Filters

```shell
rclone sync "/local/path" "remote":"/remote/path" --exclude "node_modules/"
```

## Mount

- Mount remote to a mount point
- Requires `fuse2` package

```shell
# mount
rclone mount "remote":"/remote/path" "/local/path"
rclone mount hvitoi:/ /mnt/hvitoi
```

## Crypt remote

- `crypt` remote takes another remote as part of its configuration
- It encrypts data and hands it over to the underlying remote
- Everything crypt does is to encrypt and decrypt data

1. Create new remote
1. Choose type "crypt" (Encrypt/Decrypt a remote)
1. Select the origin remote
1. Create passwords
1. Done

```shell
# checks a remote against a crypted remote. It works by reading the nonce from each file on the crypted remote
rclone cryptcheck "/path/to/files" "remote-crypt:path"
```
