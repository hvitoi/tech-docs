# gzip

- Compress or uncompress a file

```shell
# Compress file and saves it to itself
gzip "file.tar" # output "file.tar.gz"
gzip "file" # output file.gz

# Uncompress and saves it to itself
gzip -d "file.tar.gz" # output "file.tar"
gzip -d "file.gz" # output "file"
```
