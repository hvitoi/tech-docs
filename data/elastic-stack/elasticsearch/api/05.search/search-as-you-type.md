# Search as you type

## Create analyzer

```sh
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

## Update mapping configuration

```sh

# Update configuration
curl -s 'localhost:9200/autocomplete' \
  --request PUT \
  --header "Content-Type: application/json" \
  --data @configuration.json \
| jq .

```

```json
{
  "mappings": {
    "properties": {
      "title": {
        "type": "search_as_you_type"
      },
      "genre": {
        "type": "search_as_you_type"
      }
    }
  }
}
```

## Reindex

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

## Search

```sh
curl -s "localhost:9200/autocomplete/_search" \
  --request GET \
  --header "Content-Type: application/json" \
  --data @search.json \
| jq .
```

```json
{
  "size": 5,
  "query": {
    "multi_match": {
      "query": "Sta",
      "type": "bool_prefix",
      "fields": ["title", "title._2gram", "title._3gram"]
    }
  }
}
```

## Search while typing

```sh
while true
do
  IFS= read -rsn1 char
  INPUT=$INPUT$char
  echo $INPUT
  curl -s -X GET 'http://localhost:9200/autocomplete/_search' \
    --data '
      {
        "size": 5,
        "query": {
          "multi_match": {
            "query": "'"$INPUT"'",
            "type": "bool_prefix",
            "fields": [
              "title",
              "title._2gram",
              "title._3gram"
            ]
          }
        }
      }
    ' \
  | jq .hits.hits[]._source.title \
  | grep -i "$INPUT"
done
```
