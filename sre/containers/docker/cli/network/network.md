# docker network

- `bridge`: virtual bridge network with private addresses (172.17.0.0). `docker0` is the bridge network on the host (ip link add docker0 type bridge). A namespace for each container is created and attached to the bridge net
- `host`: container shares the host network (192.168.0.0)
- `none`: containers cannot talk to each other or to the host
- `overlay`: talk to nodes across nodes! Good for swarm. All the ips work as one!

```shell
# Lists networks
docker network ls

# Create new network
docker network create "network-name" # bridge driver by default
docker network create --driver "net-type" "network-name"

# Connect container to a network
docker network connect "network" "container"

## Disconnect container from a network
docker network disconnect "network" "container"

## Inspect a network
docker network inspect "network" # show all containers attached to that network
```

- **Docker DNS**: It's possible to ping other containers by its container name
- **DNS Round Robit**: Multiple IPs for the same name
