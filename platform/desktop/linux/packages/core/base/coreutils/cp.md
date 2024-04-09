# Copy

```shell
# Copy a file
cp "file" "new-file"
cp ~/.bashrc bashrc.bak

# Copy to different location
cp ~/ola.txt ~/novo/novo_ola.txt
cp ~/ola.txt ~/novo # copies as ola.txt in ~/novo dir)

# Copy a directory
cp -r "dir" "new-dir"
cp -rv "dir" "new-dir" # verbose

# Create directories as needed
mkdir -p /foo/bar && cp myfile "$_"
```
