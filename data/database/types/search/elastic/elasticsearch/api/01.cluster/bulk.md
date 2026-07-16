# JSON bulk import

- Import many documents at once
- The index for each data can be specified

```shell
curl -s 'localhost:9200/_bulk' \
  --request PUT \
  --header "Content-Type: application/json" \
  --data-binary @dataset.json
```

## Bulk json

- `1st line`: Info about where to insert the document (Exact shard)
- `2nd line`: Document data itself

```json
{ "create" : { "_index" : "movies", "_id" : "135569" } }
{ "id": "135569", "title" : "Star Trek Beyond", "year":2016 , "genre":["Action", "Adventure", "Sci-Fi"] }
```
