# match_all

```sh
curl -s "localhost:9200/movies/_search" \
  --request GET \
  --header "Content-Type: application/json" \
  --data @search.json \
| jq .
```

- It's the default option (usually not even specified)
- Returns all documents. Normally used with a filter

```json
{
  "query": {
    "match_all": {}
  }
}
```
