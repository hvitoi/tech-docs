# grep

- Global regular expression print
- Print lines that match a specified pattern

```shell
# Create sample file
echo "a b c" > "file.txt"
```

```shell
# General usage
grep "keyword" "file"

# Parameters
grep -q "keyword" "file" # quiet mode
grep -c "keyword" "file" # Count matching lines
grep -n "keyword" "file" # Display matching lines and show its number
grep -i "keyword" "file" # Case insensitive
grep -v "keyword" "file" # Intersection. Exclude the line that do not contain the keyword
grep -w "keyword" "file" # Match only whole words
grep -e "bluez" -e "a2dp_codec" "file" # regex patterns
grep -iE "installed|upgraded|removed" "/var/log/pacman.log" # extended regex
grep -A5 "keyword" "file" # print 5 lines underneath the keyword
grep -B5 "keyword" "file" # print 5 lines above the keyword

# Find in all file contents (excluding binaries and ignoring case)
grep -RIi "hvitoi" "." # look for the keyword "hvitoi" in all file content inside of the current directory

# Pipe
ls -l ~/ | grep Desktop
```
