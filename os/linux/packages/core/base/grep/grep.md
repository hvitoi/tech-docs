# grep

- Global regular expression print
- Print lines that match a specified pattern

```shell
# Create sample file
echo "Henrique Abrantes Vitoi
Lais Abrantes Vitoi
Simone Gomes Abrantes Vitoi
Luiz Henrique Rossi Vitoi" > family
```

```shell
# General usage
grep "keyword" "file"

# Parameters
grep -c "keyword" "file" # Count matching lines
grep -n "keyword" "file" # Display matching lines and show its number
grep -i "keyword" "file" # Case insensitive
grep -v "keyword" "file" # Intersection. Exclude the line that do not contain the keyword
grep -w "keyword" "file" # Match only whole words
grep -e "bluez" -e "a2dp_codec" "file" # regex patterns
grep -iE "installed|upgraded|removed" "/var/log/pacman.log" # extended regex
grep -A5 "keyword" "file" # print 5 lines underneath the keyword

# Find in all file contents
grep -R "hvitoi" "." # look for the keyword "hvitoi" in all file content inside of the current directory

# Pipe
ls -l ~/ | grep Desktop
```
