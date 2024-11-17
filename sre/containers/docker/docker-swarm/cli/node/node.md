# docker node

- The node is the physical machine

## ls

- List all nodes

```shell
docker node ls
```

## ps

- Processes in the node

```shell
docker node ps "my-node"
```

## update

```shell
# Update role of a node
docker node update \
  --role "manager" \
  "my-node"
```
