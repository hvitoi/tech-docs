# fish

## Builtin commands

### set

- Set/unset shell variables

```shell
# Export variables to child processes
set -x key value
set -xg key value # global (global within a shell session)
set -xl key value # local (erased when the block ends)

# Erase variables
set -e key

# Check if a variable is defined
set -q key
```

```shell
key=value echo $key
begin; set -lx key value; echo $key; end
```

### status

```shell
# check properties of the currently opened shell
status --is-interactive
status --is-login
```
