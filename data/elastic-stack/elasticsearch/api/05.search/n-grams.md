# n-grams

- `unigram`: [ s, t, a, r ]
- `bigram`: [ st, ta, ar ]
- `trigram`: [ sta, tar ]
- `4-gram`: [ star ]

## Index configuration

- Create custom autocomplete analyzer
- Set up mapping configuration

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

## Query

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
    "match": {
      "title": {
        "query": "sta",
        "analyzer": "standard"
      }
    }
  }
}
```
