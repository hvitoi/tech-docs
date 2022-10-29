# Aggregation functions

- size=0 shows only the aggregations and not the results

```sh
curl -s "localhost:9200/ratings/_search?size=0" \
  --request GET \
  --header "Content-Type: application/json" \
  --data @search.json \
| jq .
```

## Average

- Example take the Star Wars IV films and measure the average rating

```json
{
  "query": {
    "match_phrase": {
      "title": "Star Wars Episode IV"
    }
  },
  "aggs": {
    "avg_rating": {
      "avg": {
        "field": "rating"
      }
    }
  }
}
```

## Count

- Count 5.0 rating movies

```json
{
  "query": {
    "match": {
      "rating": 5.0
    }
  },
  "aggs": {
    "ratings": {
      "terms": {
        "field": "rating"
      }
    }
  }
}
```

## Histogram

- Aggregate data by value range

```json
{
  "aggs": {
    "whole_ratings": {
      "histogram": {
        "field": "rating",
        "interval": 1.0
      }
    }
  }
}
```

## Time series

- Aggregate fields that contain time and dates

```json
{
  "aggs": {
    "timestamp": {
      "date_histogram": {
        "field": "@timestamp",
        "interval": "hour"
      }
    }
  }
}
```

```json
{
  "query": {
    "match": {
      "response": "500"
    }
  },
  "aggs": {
    "timestamp": {
      "date_histogram": {
        "field": "@timestamp",
        "interval": "minute"
      }
    }
  }
}
```

## Nested Aggregations

- Aggregation on text fields don't work well

```sh
curl -s 'localhost:9200/movies' \
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

```json
{
  "query": {
    "match_phrase": {
      "title": "Star Wars"
    }
  },
  "aggs": {
    "titles": {
      "terms": {
        "field": "title.raw"
      },
      "aggs": {
        "avg_rating": {
          "avg": {
            "field": "rating"
          }
        }
      }
    }
  }
}
```
