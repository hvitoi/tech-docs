# echo

- There is also the shell built-in command echo

```shell
# Prints a text
echo "hey"

echo {1..10..1} # 1 to 10

# Don't add line breaks
echo -n "Hey, there" # ends with a % (identify that it doesn't have a line break at the end)

# Enable interpretation of special characters
echo -e "Hey, there\0"

NO_FORMAT="\033[0m"
C_GREEN="\033[38;5;2m"
echo -e "${C_GREEN}Put some color on me${NO_FORMAT}"

# Add Text to Files
echo "This text replaces everything" > text.txt
echo "This text is appended" >> text.txt

# Add commands to echo
echo "The current date is $(date)."

# Output of a command into a text file
ls -l > text.txt
```
