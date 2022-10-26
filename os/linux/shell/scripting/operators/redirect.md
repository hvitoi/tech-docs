# Redirect operator

- Standard input (`stdin`): file descriptor number `0`
- Standard output (`stout`): file descriptor number `1`
- Standard error (`stderr`): file descriptor number `2`

## Redirect

```sh
echo "hello" > "output.txt" # redirects stdout
echo "hello" 1> "output.txt" # redirects stdout
echo "hello" 2> "error.txt" # redirects stderr
echo "hello" &> "out-err.txt" # redirects stdout and stderr
echo "hello" > "out-err.txt" 2>&1 # redirects stdout and stderr (deprecated)
```

```sh
# Stdin comes from a file content
mail -s "Office memo" "mail@mail.com" < "memoletter.txt"
```

```sh
cat "file"
cat 0< "file.txt" # cat from stdin
cat 0< "file.txt" 1> "/dev/stout"  # cat from stdin to stout
```

## Append

```sh
echo "hello" > "file.txt" # append hello to the file
```

## Exit Code

```sh
# Show exit code from previous command
echo $?
```

```sh
cat "/dev/stdin"
cat "/dev/stdout"
cat "/dev/stderr"
```

```sh
# Send exit code to 2>/dev/null
# If there is error (||) return exit code success. (|) would always return success
cp ./a ./b 2> /dev/null || :
```
