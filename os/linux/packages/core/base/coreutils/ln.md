# ln - Link

- `Inode`: Address of the file on the hard disk
- `Symbolic link`: Link is removed if file removed or renamed. The soft link has different inode from the original file
- `Hard link`: Deleting/renaming/moving the original file does not affect the link. Connects to inode. Hard link only works in the same partition. Hard link connects straight to the inode. A hard link is just the same file (not treated with a link - L)

```shell
# List the inodes in a directory
ls -li # i stands for inode

# Create a symbolic link
ln -s "original-file-path" "soft-link-path"

# Create a hard link
ln "original-file-path" "hard-link-path"
```
