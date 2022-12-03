# Redirect operator

- Standard input (`stdin`): file descriptor number `0`
- Standard output (`stout`): file descriptor number `1`
- Standard error (`stderr`): file descriptor number `2`

## Redirect

```shell
echo "hello" > "output.txt" # redirects stdout
echo "hello" 1> "output.txt" # redirects stdout
echo "hello" 2> "error.txt" # redirects stderr
echo "hello" &> "out-err.txt" # redirects stdout and stderr
echo "hello" > "out-err.txt" 2>&1 # redirects stdout and stderr (deprecated)
```

```shell
# Stdin comes from a file content
mail -s "Office memo" "mail@mail.com" < "memoletter.txt"
```

```shell
cat "file"
cat 0< "file.txt" # cat from stdin
cat 0< "file.txt" 1> "/dev/stout"  # cat from stdin to stout
```

## Append

```shell
echo "hello" > "file.txt" # append hello to the file
```

## Exit Code

```shell
# Show exit code from previous command
echo $?
```

```shell
cat "/dev/stdin"
cat "/dev/stdout"
cat "/dev/stderr"
```

```shell
# Send exit code to 2>/dev/null
# If there is error (||) return exit code success. (|) would always return success
cp ./a ./b 2> /dev/null || :
```
