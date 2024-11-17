# docker swarm

## init

```shell
# Check if swarm is active
docker info

# Enable swarm
docker swarm init
docker swarm init --advertise-addr <ip> # specify an ip for the node
```

## leave

```shell
# Leave a swarm
docker swarm leave
```

## join

- Join an existing swarm
- As a worker. Wokers can't run swarm commands

```shell
docker swarm join \
    --token <token> \
    <ip>:<port>
```

## join-token manager

- Create a token for a manager node

```shell
docker swarm join-token manager
```
