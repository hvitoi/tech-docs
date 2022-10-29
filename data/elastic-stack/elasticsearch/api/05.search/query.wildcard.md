# wildcard

- Search with a wildcard
- Prefix can only be used on `keyword`, `text` and `wildcard` fields
- A full `regex` rule can also be specified

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
    "wildcard": {
      "genre": "Advent*"
    }
  }
}
```
