# Sort

- Sort can only be performed by `not_analyzed` fields. E.g. `keyword`

```shell
curl -s "localhost:9200/movies/_search" \
  --request GET \
  --header "Content-Type: application/json" \
  --data @search.json \
| jq .
```

```json
{
  "sort": "year"
}
```

```json
{
  "sort": {
    "@timestamp": {
      "order": "asc"
    }
  }
}
```

## New field for not_analyzed data

- Create new subfield "raw" to be used for sorting purposes

```shell
curl -s "localhost:9200/movies" \
  --request PUT \
  --header "Content-Type: application/json" \
  --data '
  {
    "mappings": {
      "properties": {
        "title": {
          "type": "text",
          "fields": {
            "raw": {
              "type": "keyword"
            }
          }
        }
      }
    }
  }
  ' \
| jq .
```
