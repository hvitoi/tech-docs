# Kibana installation

- default port: `5601`

## Debian

- Configuration file: `/etc/kibana/kibana.yml`

```sh
sudo apt install kibana
sudo systemctl start kibana
```

## Docker

- Documentation: <https://www.elastic.co/guide/en/kibana/current/docker.html>
- Configuration file: `/usr/share/kibana/config/kibana.yml` or with environment variables

```sh
docker container run \
  --rm \
  -it \
  docker.elastic.co/kibana/kibana:7.10.1
```
