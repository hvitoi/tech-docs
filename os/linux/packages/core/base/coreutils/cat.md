# cat

- Stands for con**cat**enate

```sh
# Print the content of a file
cat "file"
cat 0< "file.txt" # cat from stdin
cat 0< "file.txt" 1> "/dev/stout"  # cat from stdin to stout

# Open prompt to append text to "file". Ctrl+D to finish
cat >> "file"

# Open prompt to completely replace text of "file"
cat > "file"

# Concatenate both files, but does not save
cat "file1" "file2"

# Concatenate by wild card
cat "file*"

# Combine file
cat "file1" "file2" > "new-file" # Does not modify the original files
```

```sh
# cat with line numbers
cat -n "file.txt"

# adds a dollar sign at every end of line
cat -E "file.txt"

# tabs as ^I
cat -T "file.txt"
```
