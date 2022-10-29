# prefix

- Prefix search
- Prefix can only be used on `keyword`, `text` and `wildcard` fields

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
    "prefix": {
      "genre": "Advent"
    }
  }
}
```
