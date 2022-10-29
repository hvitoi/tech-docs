# Logstash installation

## Debian

- Configuration file: `/etc/logstash/conf.d/logstash.yml`
- Pipeline: `/etc/logstash/conf.d/logstash.conf`

```sh
sudo apt install openjdk-8-jre-headless
sudo apt install logstash
sudo bin/logstash -f /etc/logstash/conf.d/logstash.conf
```

```sh
sudo bin/logstash --path.settings `/etc/logstash/conf.d/logstash.yml` -f `/etc/logstash/conf.d/logstash.conf`
```

## Docker

- Configuration file: `/usr/share/logstash/config/logstash.yml`
  - Configuration can be set by means of environment variables!
- Pipelines: `/usr/share/logstash/pipeline/logstash.conf`

```sh
docker container run \
  --rm \
  -it \
  -v ~/pipeline/:/usr/share/logstash/pipeline/ \
  docker.elastic.co/logstash/logstash:7.10.1
```
