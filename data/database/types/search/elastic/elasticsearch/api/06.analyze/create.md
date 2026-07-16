# Create analyzer

```shell
curl -s "localhost:9200/movies/_analyze" \
  --request POST \
  --header "Content-Type: application/json" \
  --data @analyze.json \
| jq .
```

```json
{
  "tokenizer": "standard",
  "filter": [
    {
      "type": "edge_ngram",
      "min_gram": 1,
      "max_gram": 4
    }
  ],
  "text": "Star"
}
```
