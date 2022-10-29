# Metric beat

- Collect metrics from your system and services (cpu, memory, redis, nginx, etc)
- Send system and service statistics to ES and others

## Installation Docker

- Provide configuration by arguments

```sh
docker container run \
  docker.elastic.co/beats/metricbeat:7.10.1 \
    setup -E setup.kibana.host=kibana:5601 -E output.elasticsearch.hosts=["elasticsearch:9200"]
```

- Provide configuration file `/usr/share/metricbeat/metricbeat.yml`

```sh
docker run -d \
  --name=metricbeat \
  --user=root \
  --volume="$(pwd)/metricbeat.docker.yml:/usr/share/metricbeat/metricbeat.yml:ro" \
  --volume="/var/run/docker.sock:/var/run/docker.sock:ro" \
  --volume="/sys/fs/cgroup:/hostfs/sys/fs/cgroup:ro" \
  --volume="/proc:/hostfs/proc:ro" \
  --volume="/:/hostfs:ro" \
  docker.elastic.co/beats/metricbeat:7.10.1 metricbeat -e \
  -E output.elasticsearch.hosts=["elasticsearch:9200"]
```
