# Redis container install

```shell
# Pull, Build and Run
docker pull redis

# docker build -t hvitoi/mysql .
docker run --name meu_redis --rm -d -v $(pwd)/dados:/data -p 6379:6379 redis redis-server --appendonly yes

# Execute
docker exec -it meu_redis /bin/bash
docker exec -it meu_redis redis-cli

# Stop, Remove, Remove Image
docker stop meu_redis
docker rm meu_redis
docker rmi redis
```
