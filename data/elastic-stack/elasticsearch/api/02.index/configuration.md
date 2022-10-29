# Index configuration

```sh
# Get index configuration
curl -X GET "localhost:9200/movies?pretty"

# Get specific configuration
curl -X GET "localhost:9200/movies/_alias?pretty"
curl -X GET "localhost:9200/movies/_mappings?pretty"
curl -X GET "localhost:9200/movies/_settings?pretty"

# Update configuration (or create index)
curl -X PUT "localhost:9200/movies" \
  --header "Content-Type: application/json" \
  --data @configuration.json

# Delete the whole index
curl -X DELETE "localhost:9200/movies"
```

## Alow invalid documents

- The index must be `_close` (before) and `_open` (after)

```json
{
  "index.mapping.ignore_malformed": true
}
```

## Increase total fields

```json
{
  "index.mapping.total_fields.limit": 1001
}
```

## Create an "autocomplete" analyzer

```json
{
  "settings": {
    "analysis": {
      "filter": {
        "autocomplete_filter": {
          "type": "edge_ngram",
          "min_gram": 1,
          "max_gram": 20
        }
      },
      "analyzer": {
        "autocomplete": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "autocomplete_filter"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "autocomplete"
      }
    }
  }
}
```

## Mapping

```json
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "fielddata": true,
        "fields": {
          "raw": {
            "type": "keyword"
          }
        }
      }
    }
  }
}
```
