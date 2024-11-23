# Find

## -print

- Just print the filename
- This is the default action when none is provided

```shell
find . -print
find . # same!
```

## -type

- Search by file type

```shell
file . -type f # file
file . -type d # directory
```

## -name

- Search by file name

```shell
find . -name notes.txt
find . -iname notes # include name
```

## -delete

```shell
# delete files with a name
find . -name "package-lock.json" -type f -delete

# delete empty directories
find . -type d -empty -delete
```

## -prune

```shell
find . -name "node_modules" -type d -prune # list
find . -name "node_modules" -type d -prune -exec rm -rf "{}" + # delete
```

## -empty

- Find empty

```shell
# Find empty directories
find . -type d -empty
```

## -path

- Exclude a path from search

```shell
find . -not -path "/home/*" # find everything that is not in the home folder
find . ! -path "/home/*" ! -path "/proc/*" # exclude multiple folders
```

## -nogroup

- Files without group (group has been removed)

```shell
find . -nogroup -ls
```

## -regex

```shell
find . -regex ".*\(aaa\|bbb\).*\.so" -exec cp {} {}.bak \;
```
