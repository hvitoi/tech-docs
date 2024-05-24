# getconf

## PAGE_SIZE

- 4K This size has been a standard choice for many years due to its balance between memory management efficiency and system performance
- Linux ARM64 software is compatible with 16K pages (and 64K pages) by default

```shell
getconf PAGE_SIZE
```
