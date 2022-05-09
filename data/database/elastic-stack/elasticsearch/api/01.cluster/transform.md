# Dataframe transforms

- Define the mechanism to aggregate data
- **Why transform**?

  - Performance: aggregation functions get rerun everytime
  - Result limitation
  - Dimensionality of data

- **How to transform?**
  - Through API or Kibana
    1. `Define`
    - Identifier
    - Source
    - Pivot
    - Destination
    1. `Run`
    - Destination index
    - Assurance validations
    - Checkpoint

## Example

### Mapping

```shell
curl -s "http://localhost:9200/nginx" \
  --request PUT \
  --header 'Content-Type: application/json' \
  --data @configuration.json
```

```json
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  },
  "mappings": {
    "properties": {
      "time": { "type": "date", "format": "dd/MMM/yyyy:HH:mm:ss Z" },
      "remote_ip": { "type": "ip" },
      "remote_user": { "type": "keyword" },
      "request": { "type": "keyword" },
      "response": { "type": "keyword" },
      "bytes": { "type": "long" },
      "referrer": { "type": "keyword" },
      "agent": { "type": "keyword" }
    }
  }
}
```

### Transform preview

```shell
curl --location --request POST -H 'Content-Type:application/json' 'http://localhost:9200/_transform/_preview' \
--data-raw '{
   "source": {
       "index": "nginx"
   },
   "pivot": {
       "group_by": {
           "ip": {
               "terms": {
                   "field": "remote_ip"
               }
           }
       },
       "aggregations": {
           "bytes.avg": {
               "avg": {
                   "field": "bytes"
               }
           },
           "bytes.sum": {
               "sum": {
                   "field": "bytes"
               }
           },
           "requests.total": {
               "value_count": {
                   "field": "_id"
               }
           },
           "requests.last": {
               "scripted_metric": {
                   "init_script": "state.timestamp = 0L; state.date = '\'''\''",
                   "map_script": "def doc_date = doc['\''time'\''].getValue().toInstant().toEpochMilli();if (doc_date > state.timestamp){state.timestamp = doc_date;state.date = doc['\''time'\''].getValue();}",
                   "combine_script": "return state",
                   "reduce_script": "def date = '\'''\'';def timestamp = 0L;for (s in states) {if (s.timestamp > (timestamp)){timestamp = s.timestamp; date = s.date;}} return date"
               }
           },
           "requests.first": {
               "scripted_metric": {
                   "init_script": "state.timestamp = 1609455599000L; state.date = '\'''\''",
                   "map_script": "def doc_date = doc['\''time'\''].getValue().toInstant().toEpochMilli();if (doc_date < state.timestamp){state.timestamp = doc_date;state.date = doc['\''time'\''].getValue();}",
                   "combine_script": "return state",
                   "reduce_script": "def date = '\'''\'';def timestamp = 0L;for (s in states) {if (s.timestamp > (timestamp)){timestamp = s.timestamp; date = s.date;}} return date"
               }
           }
       }
   }
}'
```

### Transform

```shell
curl --location --request PUT -H 'Content-Type:application/json' 'http://localhost:9200/_transform/nginx_transform' \
--data-raw '{
   "source": {
       "index": "nginx"
   },
   "pivot": {
       "group_by": {
           "ip": {
               "terms": {
                   "field": "remote_ip"
               }
           }
       },
       "aggregations": {
           "bytes.avg": {
               "avg": {
                   "field": "bytes"
               }
           },
           "bytes.sum": {
               "sum": {
                   "field": "bytes"
               }
           },
           "requests.total": {
               "value_count": {
                   "field": "_id"
               }
           },
           "requests.last": {
               "scripted_metric": {
                   "init_script": "state.timestamp = 0L; state.date = '\'''\''",
                   "map_script": "def doc_date = doc['\''time'\''].getValue().toInstant().toEpochMilli();if (doc_date > state.timestamp){state.timestamp = doc_date;state.date = doc['\''time'\''].getValue();}",
                   "combine_script": "return state",
                   "reduce_script": "def date = '\'''\'';def timestamp = 0L;for (s in states) {if (s.timestamp > (timestamp)){timestamp = s.timestamp; date = s.date;}} return date"
               }
           },
           "requests.first": {
               "scripted_metric": {
                   "init_script": "state.timestamp = 1609455599000L; state.date = '\'''\''",
                   "map_script": "def doc_date = doc['\''time'\''].getValue().toInstant().toEpochMilli();if (doc_date < state.timestamp){state.timestamp = doc_date;state.date = doc['\''time'\''].getValue();}",
                   "combine_script": "return state",
                   "reduce_script": "def date = '\'''\'';def timestamp = 0L;for (s in states) {if (s.timestamp > (timestamp)){timestamp = s.timestamp; date = s.date;}} return date"
               }
           }
       }
   },

    "description": "Bytes and request dates overview for remote_ip",
    "dest": {
      "index": "nginx_transformed"
    }

}'
```

### Start transform

```shell
curl "localhost:9200/_transform/nginx_transform/_start"  --request POST
```
