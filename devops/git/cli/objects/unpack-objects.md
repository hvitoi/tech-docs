# Git pack file

- pack file is a single file that stores all the objects and optimizes space

```sh
# Unpack and create a conventional "objects" folder
cat `file.pack` | git unpack-objects
```
