# Pagination

- Pagination shows a number of results per page
- `from`: start point (0 indexed)
- `size`: number of results per page

```shell
curl -s "localhost:9200/movies/_search" \
  --request GET \
  --header "Content-Type: application/json" \
  --data @search.json \
| jq .
```

```json
{
  "from": 2,
  "size": 2,
  "query": {
    "match": {
      "genre": "Sci-Fi"
    }
  }
}
```
