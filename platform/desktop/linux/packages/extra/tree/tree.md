# tree

- Directory listing program displaying a depth indented list of files
- Display directories and subdirectories as a nesting tree; like ls but recursive

```shell
tree # current folder
tree <folder> # specific folder

# Hidden files
tree -a

# Depth
tree -L "3"

# Directories only
tree -d

# File sizes
tree -s
tree -h # human readable sizes

# File permissions
tree -p

# Shows full path
tree -f # relative path
tree -f $PWD # absolute path

# Exclude mounted filesystems
tree -x
```
