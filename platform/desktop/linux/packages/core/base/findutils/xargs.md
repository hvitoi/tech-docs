# xargs

- Useful for piping command together but the commands do not accept piped input
- `xargs` can take the output from one command and send it to another command as parameters.
- `xargs` accepts piped input or file input and uses it to feed another command

```shell
# just echo it out as an array (even if the input is multiline)
ls -1 | xargs
ls -1 | xargs echo # same
```

```shell
# ask for confirmation
echo 'one two three' | xargs -p

# interaction
echo "package1 package2 package3" | xargs -ro echo

# substitution
echo "Henry" | xargs -I "{}" echo 'I am {}!'
xargs -I "{}" echo Blah {} blabla {} < <(seq 1 5)
xargs -I "{}" echo "Item" {} < items.txt

# multiple substitutions
xargs -I % sh -c 'echo %; mkdir %' < directories.txt

# stdin
dmenu_path | dmenu | xargs swaymsg exec --
```
