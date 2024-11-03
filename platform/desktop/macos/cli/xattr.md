# xattr

- Manages `extended attributes` associated with a file or directory
- The presence of extended attributes are typically noted by the `@` symbol

```txt
drwx------@  2 john    staff    64B Nov  3 16:44 file.txt
```

## -l

```shell
# list extended attributes
xattr -l file.txt
```

## -d

```shell
# Remove attribute
xattr -d "com.apple.quarantine" file.txt
xattr -d "com.apple.provenance" file.txt
```

## -c

```shell
# Remove att attributes
xattr -c file.txt
```
