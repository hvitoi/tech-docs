# Kibana Canvas

- Present ES data with live infographic dashboard
- Canvas components
  - Workpad
  - Page
  - Elements: `Charts`, `Shapes`, `Images`, `Supporting elements`
- Data source: `ES SQL queries`, `Timelion expressions`, `Raw documents`

- Convert nginx json logs into bulk format

```sh
awk '{print "{\"index\":{}}\n" $0}' nginx_json_logs > nginx_json_logs_bulk
```

- Mapping

```sh
curl -s "http://localhost:9200/nginx" \
  --request PUT \
  --header 'Content-Type: application/json' \
  -d '{
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "time": {"type":"date","format":"dd/MMM/yyyy:HH:mm:ss Z"},
            "response": {"type":"keyword"}
        }
    }
  }'
```

- Import data

```sh
curl -s  'http://localhost:9200/nginx/_doc/_bulk' \
  --request POST \
  --header 'Content-Type: application/x-ndjson' \
  --data-binary @nginx_json_logs_bulk \
| jq '.errors'
```

## Expression editor

```canvas
filters
| essql
  query="SELECT SUM(bytes) AS total_transferred_top5 FROM nginx GROUP BY remote_ip ORDER BY total_transferred_top5 DESC NULLS LAST LIMIT 5"
| math "mean(percent_uptime)"
| progress shape="gauge" label={formatnumber "0%"}
  font={font size=24 family="'Open Sans', Helvetica, Arial, sans-serif" color="#000000" align="center"}
| render
```
