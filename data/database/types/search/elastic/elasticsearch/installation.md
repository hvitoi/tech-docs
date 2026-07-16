# Elasticsearch installation

## Debian package

- Configuration file: `/etc/elasticsearch/elasticsearch.yml`

```shell
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add - # Import PGP key
sudo apt-get install apt-transport-https
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
vecho "deb https://artifacts.elastic.co/packages/oss-7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list # Only open source
sudo apt-get update && sudo apt-get install elasticsearch
```

## Docker

- Configuration file: `/usr/share/elasticsearch/config/elasticsearch.yml`
  - Configuration can be set by means of environment variables!

```shell
docker container run \
  --name elasticsearch \
  -p 9200:9200 -p 9300:9300 \
  -e "discovery.type=single-node" \
  docker.elastic.co/elasticsearch/elasticsearch:7.10.1
```

## Testing connection

```shell
curl -XGET localhost:9200
```
