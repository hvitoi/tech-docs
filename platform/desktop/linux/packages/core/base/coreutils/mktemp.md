# mktemp

- Outputs the path of the file/folder created

```shell
# Temporary file
temp_file=$(mktemp)

# Specify the filename, but use the default temp directory
mktemp foo.txt --tmpdir

# Temporary directory
temp_dir=$(mktemp -d)
```
