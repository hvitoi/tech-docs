# docker network create

- Create a new network

```shell
docker network create "network-name" # bridge driver by default
docker network create --driver "net-type" "network-name"
```

## Drivers

- `bridge`: virtual bridge network with private addresses (172.17.0.0). `docker0` is the bridge network on the host (ip link add docker0 type bridge). A namespace for each container is created and attached to the bridge net
- `host`: container shares the host network (192.168.0.0)
- `none`: containers cannot talk to each other or to the host
- `overlay`: talk to nodes across nodes! Good for swarm. All the ips work as one!
