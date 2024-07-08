# kill

- Kills by the process id (pid)

```shell
# Kills a process
kill <pid>

# Choose Signal
kill -9 <pid> # SIGKILL
kill -s <signal> <pid> # SIGKILL

# Suspend a process
kill -STOP <pid>
```

## Signals

- Default signal is 15 (SIGTERM)

```shell
# List signals
kill -l

# Signals
man 7 signal
```
