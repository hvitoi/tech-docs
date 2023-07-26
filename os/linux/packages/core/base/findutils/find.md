# Find

- Find uses the "hard way". It iterates over the filesystem
- `find` searches files or directories iterating over the filesystem (slow)

## Search files and directories

```shell
# Search by file name
find "." -name "notes.txt"
find "." -iname "notes.txt" # include name

# Search by file type and file name
file "/" -type f # f for file
file "/" -type d # d for directory

# REgex
find "/" -regex ".*\(bluez5\|bluetooth\).*\.so" -exec cp {} {}.bak \;

# node_modules
find "." -name "node_modules" -type d -prune # list
find "." -name "node_modules" -type d -prune -exec rm -rf "{}" + # delete

# Files without group (group has been removed)
sudo find / -nogroup -ls

# Find empty directories
find . -type d -empty -print
find . -type d -empty -delete
```
