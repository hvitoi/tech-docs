# multi_match

- Run the same query on multiple fields

```shell
curl -s "localhost:9200/movies/_search" \
  --request GET \
  --header "Content-Type: application/json" \
  --data @search.json \
| jq .
```

```json
{
  "query": {
    "multi_match": {
      "query": "star",
      "fields": ["title", "synopsis"]
    }
  }
}
```
