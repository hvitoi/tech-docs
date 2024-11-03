# nohup

- Send a process to the background
- It's not like the `bg/&` command that ties the process to a terminal session. With nohup the command is executed like a system daemon

```shell
# Stores the execution logs at "./nohup.out"
nohup sleep 9999
nohup sleep 9999 & # also detach the nohup from stdin

# do not save logs
nohup sleep 9999 &> /dev/null &
```
