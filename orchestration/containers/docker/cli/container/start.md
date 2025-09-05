# docker container start

- Accepts only a few options (not like `container run`)
- With `start` it's not possible to replace the CMD defined at the container creation
- By default starts the container detached (use -a to attach it)

```shell
docker container start <container>
docker container start -a <container> # attach container's STDOUT and STDERR
docker container start -i <container> # keep STDIN open even if not attached
```
