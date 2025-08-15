# Input Redirection "n< file"
# Redirect to stdin
# Changes the file descriptor 0 (stdin)

# stdin from file
cat 0<"file.txt"
cat <"file.txt"

# cat from stdin to stout
cat 0<"file.txt" 1>"/dev/stout"

# Stdin from a file content
mail -s "Office memo" "mail@mail.com" <"memoletter.txt"

xargs -I "{}" echo Blah {} blabla {} < <(seq 1 5)

KEYS=$(<test.json jq -r '.keys | @sh')
echo "${KEYS[@]}"
