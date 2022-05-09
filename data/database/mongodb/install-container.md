# MongoDB container installation

```sh
# Pull, Build and Run
docker pull mongo
docker run --name meu_mongo -d -v /home/hvitoi/data/mongo:/data -p 27017:27017 mongo

# Execute
docker exec -it meu_mongo mongo

# Stop, Remove, Remove Image
docker stop meu_mongo
docker rm meu_mongo
docker rmi mongo
```
