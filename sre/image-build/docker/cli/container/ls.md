# docker container ls

```shell
# List containers
docker container ls
docker container ls --all # -a
docker ps # Legacy

docker container ls -q # only the container ids
docker image rm $(docker container ls -a -q)
```
