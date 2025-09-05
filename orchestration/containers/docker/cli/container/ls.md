# docker container ls

```shell
docker container ls
docker ps # legacy
```

## --all

- Lists all containers, including those already exited

```shell
docker container ls --all # -a
```

## --quiet

- Shows only the container ids

```shell
docker container ls -q
docker container rm $(docker container ls -a -q) # remove all containers
```

## --filter

- Filter containers matching a criteria

```shell
docker container ls --all --quiet --filter 'name=^arch$'
```
