# Shakespeare

## Download schema and documents

```sh
# Download
curl -O http://media.sundog-soft.com/es7/shakes-mapping.json # Schema
curl -O http://media.sundog-soft.com/es7/shakespeare_7.0.json # Data
```

## Apply schema and import documents

```sh
curl -H "Content-Type: application/json" -X PUT localhost:9200/shakespeare --data-binary @shakes-mapping.json
curl -H "Content-Type: application/json" -X POST localhost:9200/shakespeare/_bulk --data-binary @shakespeare_7.0.json
```

## Search

```sh
# Search "to be or not to be"
curl \
  -H "Content-Type: application/json" \
  -X GET "localhost:9200/shakespeare/_search?pretty" \
  -d '
      {
        "query": {
          "match_phrase": {
            "text_entry": "to be or not to be"
          }
        }
      }
    '
```
