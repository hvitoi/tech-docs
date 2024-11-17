# docker service

## ls

```shell
docker service ls
```

## create

```shell
# Create a service
docker service create <image>

docker service create --replicas 3 alpine ping 8.8.8.8
docker service create --name psql --network mydrupal -e POSTGRES_PASSWORD=mypass postgres
docker service create --name drupal --network mydrupal -p 80:80 drupal
docker service create --name search --replicas 3 -p 9200:9200 elasticsearch:2   # If ping on localhost, each time it will fall to a different node. It's the load balances

# Named volume
docker service create \
  --name db \
  --network backend \
  -e POSTGRES_PASSWORD=mypass \
  --mount type=volume,source=db-data,target=/var/lib/postgresql/data \
  postgres:9.4

# Service with secret
docker service create \
    --name psql \
    --secret psql_user \
    --secret psql_pass \
    -e POSTGRES_PASSWORD_FILE=/run/secrets/psql_pass \
    -e POSTGRES_USER_FILE=/run/secrets/psql_user \
    postgres
```

## rm

```shell
docker service rm <service>
```

## ps

- Show tasks for the service
- The tasks show in which node they are run. If a task fails, swarm will automatically create a new one

```shell
docker service ps <service>
```

## inspect

```shell
docker service inspect <service>
```

## logs

```shell
docker service logs <service>
```

## update

```shell
docker service update --replicas <number> <service>
docker service update --secret-rm <service>
docker service update --image <image> <service>
docker service update --publish-rm <port> --publish-add <port>:<port-virt> <service>    # Change ports
docker service update --env-add <var> <service>
docker service update --force <service>     # Replace the tasks!
```

## scale

- Scale up multiple services

```shell
docker service scale <service1>=<replicas1> <service2>=<replicas2>
```
