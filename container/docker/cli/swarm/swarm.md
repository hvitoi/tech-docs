# Swarm

## Check if swarm is active

`docker info`

## Enable swarm

`docker swarm init`

`docker swarm init --advertise-addr <ip>`

- specify an ip for the node

## Leaves a swarm

`docker swarm leave`

<!-- ------------------------- -->

# Nodes

## List all nodes

`docker node ls`

- Node is the physical machine!

## Processes in the node

`docker node ps <node>`

## Create a token for a manager node

`docker swarm join-token manager`

## Join an existing swarm

`docker swarm join --token <token> <ip>:<port>`

- As a worker. Wokers can't run swarm commands

## Update role of a node

`docker node update --role manager <node>`

<!-- ------------------------- -->

# Services

## List services

`docker service ls`

## Create a service

`docker service create <image>`

```sh
docker service create --replicas 3 alpine ping 8.8.8.8
docker service create --name psql --network mydrupal -e POSTGRES_PASSWORD=mypass postgres
docker service create --name drupal --network mydrupal -p 80:80 drupal
docker service create --name search --replicas 3 -p 9200:9200 elasticsearch:2   # If ping on localhost, each time it will fall to a different node. It's the load balances
docker service create --name db --network backend -e POSTGRES_PASSWORD=mypass --mount type=volume,source=db-data,target=/var/lib/postgresql/data postgres:9.4   # Named volume
```

## Service with secret

```sh
docker service create \
    --name psql \
    --secret psql_user \
    --secret psql_pass \
    -e POSTGRES_PASSWORD_FILE=/run/secrets/psql_pass \
    -e POSTGRES_USER_FILE=/run/secrets/psql_user \
    postgres
```

## Remove service

`docker service rm <service>`

<!-- ------------------------- -->

# Inspecting services

## Show tasks for the service

`docker service ps <service>`

- The tasks show in which node they are run. In this case in callisto! If a task fails, swarm will automatically create a new one

## Inspect a service

`docker service inspect <service>`

## Logs from service

`docker service logs <service>`

## Update the service

```sh
docker service update --replicas <number> <service>
docker service update --secret-rm <service>
docker service update --image <image> <service>
docker service update --publish-rm <port> --publish-add <port>:<port-virt> <service>    # Change ports
docker service update --env-add <var> <service>
docker service update --force <service>     # Replace the tasks!
```

## Scale up multiple services

`docker service scale <service1>=<replicas1> <service2>=<replicas2>`
