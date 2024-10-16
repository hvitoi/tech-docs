# comm

- Find common lines

```shell
# File 1
set file1 $(mktemp)
printf "%s\n" "a" "b" "c" "x" > $file1

# File 2
set file2 $(mktemp)
printf "%s\n" "a" "b" "c" "z" > $file2

# Find common lines
comm -12 $file1 $file2
```
