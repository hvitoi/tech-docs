# Data import via python script

```shell
python3 MoviesToJson.py > movies.json
```

```shell
curl -s 'localhost:9200/_bulk' \
  --request PUT \
  --header "Content-Type: application/json" \
  --data-binary @movies.json
```
