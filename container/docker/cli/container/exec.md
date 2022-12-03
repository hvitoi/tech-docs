# exec

- Execute a command on the fly in a running container

```shell
docker container exec "container-name" "command"
docker container exec -it --user "root" "container-name" "sh" # tty into container as root user
```

- STDIN
- STDOUT
- STDERR
