# diff

- File comparison

```sh
# Returns the lines that differ between the two files. Shows also the line number
diff "file1.txt" "file2.txt"

# Output diff unified context to a file
diff -u "file1.txt" "file2.txt" > changes.diff

# Compare folders
diff -bur "folder1/" "folder2/"
```

- `b` flag means ignoring whitespace
- `u` flag means a unified context (3 lines before and after)
- `r` flag means recursive

## Diff unified context

- Line 1: first file name and creation timestamp
- Line 2: second file name and creation timestamp
- Line 3: Location of the changes

```diff
--- file1.txt   2022-10-01 12:19:47.658025373 -0300
+++ file2.txt   2022-10-01 12:20:12.385773688 -0300
@@ -1,3 +1,3 @@
 Beginning of my file
-a
+b
 Ending of my file
```
