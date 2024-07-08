# fuser

- Lists open sockets and files

```shell
# Processes running in a directory
fuser -v /

# Processes using network sockets
fuser -v -n tcp 8002
```
