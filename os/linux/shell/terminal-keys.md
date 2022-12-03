# Terminal Control keys

- `C-r`: bck-i-search
- `C-l`: Clears the screen

## Processes

- `C-z`: Suspends the foreground process (SIGTSTP). Bring it back with fg
- `C-c`: Interrupt the foreground process (SIGINT)
- `C-d`: exit terminal

## Output

- `C-s`: pause a command output
- `C-q`: resume a command output

## Cut text (kill/yank)

- `C-u`: cut text from the cursor until the beginning of line
- `C-k`: cut text from the cursor until the end of line
- `C-w`: cut previous word
- `C-y`: paste back cut text

- `C-d`: remove previous character

## Navigate

- `C-a`: jump to beginning of line
- `C-e`: jump to end of line

- `C-b`: move cursor back
- `C-f`: move cursor forward

## Multiline terminal

- `C-x C-e`: Save the file to execute

```shell
for host in $HOSTS
do
  echo "${host}"
done
```
