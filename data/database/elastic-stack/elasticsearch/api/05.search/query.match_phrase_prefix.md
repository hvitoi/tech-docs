# match_phrase_prefix

- `Match phrase prefix` is used to implement a `Search as you type`

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
    "match_phrase_prefix": {
      "title": {
        "query": "star tr",
        "slop": 10
      }
    }
  }
}
```
