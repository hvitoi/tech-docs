# grep (global regular expression print)

- Global regular expression print
- Print lines that match a specified pattern

```shell
# General usage
grep "pattern" "file.txt"
cat "file.txt" | grep "keyword"

# Parameters
cat "file.txt" | grep -q "pattern" # quiet mode
cat "file.txt" | grep -c "pattern" # Count matching lines
cat "file.txt" | grep -n "pattern" # Display matching lines and show its number
cat "file.txt" | grep -i "pattern" # Case insensitive
cat "file.txt" | grep -v "pattern" # Intersection. Exclude the line that do not contain the pattern
cat "file.txt" | grep -w "pattern" # Match only whole words
cat "file.txt" | grep -f "patterns.txt" # use patterns/keywords from a file
cat "file.txt" | grep -e "bluez" -e "a2dp_codec" # regex patterns
cat "file.txt" | grep -iE "installed|upgraded|removed" # extended regex
cat "file.txt" | grep -A5 "pattern" # print 5 lines underneath the pattern
cat "file.txt" | grep -B5 "pattern" # print 5 lines above the pattern

# Find in all file contents (excluding binaries and ignoring case)
grep -RIi "hvitoi" "." # look for the pattern "hvitoi" in all file content inside of the current directory
```
