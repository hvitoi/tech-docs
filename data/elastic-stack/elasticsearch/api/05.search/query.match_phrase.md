# match_phrase

- Must find all terms, in the right order

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
    "match_phrase": {
      "title": "Star Trek"
    }
  }
}
```

## slop

- How far a term can move in order to satisfy the phrase (in either direction)
- Assigning a high scope will pick all terms and sort the results by relevance (words closer together)

```json
{
  "query": {
    "match_phrase": {
      "title": {
        "query": "star beyond",
        "slop": 1
      }
    }
  }
}
```
