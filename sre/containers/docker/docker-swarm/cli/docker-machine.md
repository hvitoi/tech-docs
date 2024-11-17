# docker-machine

- Creates multiple nodes (with busybox linux)
- Requires VM VirtualBox

## ls

- List all nodes

```shell
docker-machine ls
```

## create

```shell
docker-machine create "my-node" # default node name is "default"
docker-machine create -d "virtualbox" --virtualbox-memory "4096" --virtualbox-cpu-count "2" "my-node"
```

## start

```shell
docker-machine start "my-node"
```

## stop

```shell
docker-machine stop "my-node"
```

## rm

```shell
docker-machine rm "my-node"
```

## ssh

- SSH into a node

```shell
docker-machine ssh "my-node"
```

## env

```shell
# Show environment variables
docker-machine env "my-node"

# Exec
docker-machine env "my-node" --shell "cmd"
docker-machine env "my-node" --shell "powershell"
```

```shell
# Switch to the specified node
eval $(docker-machine env "my-node")
```
