# tail

```shell
ls -l | tail -1 # Get last line
ls -l | tail -2 # Get two last line

ls -l | tail -n +1 # Get from the first line
ls -l | tail -n +2 # Get from the second line (useful to jump headers)

# tail forever (similar to sleep infinity)
tail -f /dev/null
```
