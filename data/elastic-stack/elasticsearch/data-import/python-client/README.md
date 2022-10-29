# Data import via python script

```sh
python3 MoviesToJson.py > movies.json
```

```sh
curl -s 'localhost:9200/_bulk' \
  --request PUT \
  --header "Content-Type: application/json" \
  --data-binary @movies.json
```
