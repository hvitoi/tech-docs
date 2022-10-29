# FileBeat

- Lightweight utility that resides on the webserver to publish log data to a separate logstash cluster
- Filebeat `ships logs` to logstash
- Filebeat can optionally talk directly to elasticsearch
- The introduction to `filebeat` introduced the `elastic stack`

## Filebeat backpressure

- Filebeat maintains a read pointer to the log files running in each machine
- Filebeat cannot read faster than what logstash can handle!
- `Backpressure sensitive protocol` to tune the flux of data

## X-Pack Security

- Access Control
- Data integrity
- Audit trails

- `POST /_security/role/users`

```json
{
  "run_as": ["user_impersonator"],
  "cluster": ["movielens"],
  "indicies": [
    {
      "names": ["movies"],
      "privileges": ["read"],
      "field_security": {
        "grant": ["title", "year", "genres"]
      }
    }
  ]
}
```

## File beat installation

- `Docker`: <https://www.elastic.co/guide/en/beats/filebeat/current/running-on-docker.html>
- `Apt`: <https://www.elastic.co/guide/en/beats/filebeat/current/setup-repositories.html>

- Config file: `/usr/share/filebeat/filebeat.yml`

## Filebeat dashboards

- Install filebeat plugin for kibana

```sh
sudo filebeat setup --dashboard
```
