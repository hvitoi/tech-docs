# Copy

```shell
# Copy to different location
cp /source/file.txt /dest/file2.txt # rename it
cp /source/file.txt /dest # keep same file name

# Copy a directory
cp -r /source/dir /dest/dir # -v for verbose
cp -r /source/dir/ /dest/dir # copy only the contents (not the whole folder)

# Preserve metadata (e.g., modtime)
cp -p src dst
```
