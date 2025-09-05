# docker container exec

- Execute a command on the fly in a running container

```shell
docker container exec <container> <command>

# tty into container as root user
docker container exec -it --user "root" <container> "bash"
```
