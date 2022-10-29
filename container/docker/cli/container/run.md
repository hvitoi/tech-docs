# run

- Docker containers are Processes in the Operation System

```sh
# Run image
docker container run "image"
docker container run "image:version"
docker container run "image:version" "command"
```

```sh
# Linux Container
docker container run \
    --name "my-container" \ # container name
    --publish "3000:80" \ # map container port 3000 to host port 80
    --detach \ # run in background
    --restart "on-failure" \ # restart policy (defaults to no)
    --volume "/home/hvitoi/mydata:/var/lib/mydata" \ # volume mapping
    --env "MYSQL_ROOT_PASSWORD=123" \ # environment variables
    -build-arg JAR_FILE=build/libs/\*.jar \ # build args are reached inside the dockerfile ARG JAR_FILE ... {JAR_FILE} to use
    --network "my_net" \ # attach to a network
    --network-alias \ # net alias
    --entrypoint "echo" \ #  --rm modify default entrypoint
    --user "1001" \ # container user
    --memory "512m" \ # memory limit
    --cpu-quota "5000" \ # cpu limit (5%)
    --cap-add "MAC_ADMIN" \ # linux capabilities that can be added or removed
    --privileged \ # gives access to your host devices (can cause problems in some cases)
    --cap-add "SYS_ADMIN" \ # also access to host devices
    -w "/app" \ # set working directory
    -it \ # -t for tty, -i attach terminal to STDIN
    --rm \ # remove image after container is stopped
    "nginx" \ # image
    "Hello World!" # CMD
```

```sh
# Windows container
docker container run \
    --name "myiis" \
    -p "80:80" \
    -d \
    "mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019"
```
