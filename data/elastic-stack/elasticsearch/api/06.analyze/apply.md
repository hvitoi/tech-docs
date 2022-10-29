# Apply analyzer

```sh
curl -s "localhost:9200/movies/_analyze" \
  --request GET \
  --header "Content-Type: application/json" \
  --data @analyze.json \
| jq .
```

```json
{
  "analyzer": "autocomplete",
  "text": "Sta"
}
```
