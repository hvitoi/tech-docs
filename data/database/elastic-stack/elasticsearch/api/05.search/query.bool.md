# bool

- Bool returns true/false to a given pattern
- It's a `filter` and it's faster than the conventional match
- combine filters with boolean logic
  - `must`: AND
  - `must_not`: NOT
  - `should`: OR

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
    "bool": {
      "must": {
        "match_phrase": { "title": "Star Wars" }
      },
      "must_not": {
        "match": {
          "title": "trek"
        }
      },
      "filter": {
        "range": {
          "year": {
            "gte": 1980,
            "lt": 2010
          }
        }
      }
    }
  }
}
```

## Filters

```shell
curl "localhost:9200/movies/_search" \
  --request GET \
  --header "Content-Type: application/json" \
  --data '{
        "query": {
          "term": {
            "host.osVersion": "Bionic Beaver"
          }
        }
      }'
```

### term

- filter by exact values

```json
{
  "filter": {
    "term": {
      "year": 2014
    }
  }
}
```

### terms

- match if any exact values in a list match

```json
{
  "filter": {
    "terms": {
      "genre": ["Sci-Fi", "Adventure"]
    }
  }
}
```

### range

- find numbers or dates in a given range (gt, gte, lt, lte)

```json
{
  "query": {
    "bool": {
      "must": {
        "match_phrase": { "title": "Star Wars" }
      },
      "filter": {
        "range": {
          "year": { "gte": 1980 }
        }
      }
    }
  }
}
```

### exists

- find documents where a field exists

```json
{
  "filter": {
    "exists": {
      "field": "tags"
    }
  }
}
```

### missing

- find documents where a field is missing

```json
{
  "filter": {
    "missing": {
      "field": "tags"
    }
  }
}
```
