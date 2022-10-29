# Reindex

```sh
curl -s 'localhost:9200/_reindex' \
  --request POST \
  --header "Content-Type: application/json" \
  --data-binary @reindex.json \
| jq . \
| grep "total\|created\|failures"
```

```json
{
  "source": {
    "index": "movies"
  },
  "dest": {
    "index": "autocomplete"
  }
}
```

```sh
curl --silent --request POST 'http://localhost:9200/_reindex?pretty' --data-raw '{
 "source": {
   "index": "movies"
 },
 "dest": {
   "index": "autocomplete"
 }
}' | grep "total\|created\|failures"
```
