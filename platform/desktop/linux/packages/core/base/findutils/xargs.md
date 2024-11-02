# xargs

- Useful for piping command together but the commands do not accept piped input
- `xargs` can take the output from one command and send it to another command as parameters.
- `xargs` accepts piped input or file input and uses it to feed another command

```shell
# accepts space-separated or multiline input
echo 'one two three' | xargs # echo by default
echo 'one two three' | xargs echo # same
echo 'one two three' | xargs echo "zero" # xargs is "thread-last" by default
```

## -p (--interactive)

- Ask for confirmation

```shell
echo 'one two three' | xargs -p # y to confirm
```

## -r (--no-run-if-empty)

- Does not execute the command if the input is empty

```shell
echo "one two three" | xargs -r
echo "" | xargs -r # does not execute echo
```

## -o

- Reopen stdin as `/dev/tty` in the child process before executing the command.
- This is useful if you want xargs to run an interactive application.

```shell
echo "one two three" | xargs -o
```

## -I

- By default it is substituted in the last position (thread last)
- This flag allows replacing it anywhere in the command

```shell
echo "Henry" | xargs -I '{}' echo 'I am {}. I repeat, I am {}!'
xargs -I '{}' echo 'Number {}' < <(seq 1 5)
xargs -I '{}' echo 'Item {}' <items.txt
```
