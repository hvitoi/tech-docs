# docker-machine

- Creates multiple nodes (with busybox linux)
- Requires VM VirtualBox

```sh
# List all nodes
docker-machine ls

# Create node
docker-machine create "node-name" # default node name is "default"
docker-machine create -d "virtualbox" --virtualbox-memory "4096" --virtualbox-cpu-count "2" "node-name"

# Start node
docker-machine start "node-name"

# Stop node
docker-machine stop "node-name"

# Remove node
docker-machine rm "node-name"
```

```sh
# SSH into the node
docker-machine ssh "node-name"

# Show environment variables
docker-machine env "node-name"

# Exec
docker-machine env "node-name" --shell "cmd"
docker-machine env "node-name" --shell "powershell"
```

```sh
# Switch to the specified node
eval $(docker-machine env "node-name")
```
