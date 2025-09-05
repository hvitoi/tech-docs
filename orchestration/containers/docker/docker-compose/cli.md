# Docker Compose

- Services in the same `docker-compose` file are connected to the same network!
- Access between services are made via DNS by their service name

```shell
# List Services of the docker-compose
docker-compose ps

# Up
docker-compose up # Delete everything but the volumes
docker-compose up --build #Rebuild images and deploy
docker-compose up -d # Detached mode
docker-compose up -f "compose-file" # Specify file

# Down
docker-compose down
docker-compose down -v # Remove volumes
docker-compose down --rmi # Remove images

# Just build a Dockerfile
docker-compose build
docker-compose build --parallel

# Start / Stop
docker-compose start
docker-compose stop

# Restart a service in the compose file
docker-compose restart `service`
```
