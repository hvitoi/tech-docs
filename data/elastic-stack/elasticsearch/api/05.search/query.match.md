# match

- Search analysed results
- Supports partial hits

```sh
curl -s "localhost:9200/movies/_search" \
  --request GET \
  --header "Content-Type: application/json" \
  --data @search.json \
| jq .
```

```json
{
  "query": {
    "match": {
      "title": "star"
    }
  }
}
```
