# Movie Lens

- <https://grouplens.org/datasets/movielens/>
- Pick 100K ratings options <http://files.grouplens.org/datasets/movielens/ml-latest-small.zip>

## Download documents

```sh
curl -O http://media.sundog-soft.com/es7/movies.json
curl -O http://media.sundog-soft.com/es7/series.json
```

## Mappings

```sh
# Series
curl -X PUT localhost:9200/series \
  -H "Content-Type: application/json" \
  -d  '
      {
        "mappings": {
          "properties": {
            "film_to_franchise": {
              "type": "join",
              "relations": {
                "franchise": "film"
              }
            }
          }
        }
      }
      '
```

## Bulk import

```sh
# Movies
curl -X PUT "localhost:9200/_bulk?pretty" \
  -H "Content-Type: application/json" \
  --data-binary @movies.json

# Series
curl -X PUT "localhost:9200/_bulk?pretty" \
  -H "Content-Type: application/json" \
  --data-binary @series.json
```

## Search

```sh
# Search movie
curl -X GET "localhost:9200/movies/_search?pretty" \
  -H "Content-Type: application/json"

# Find films (child) by franchise (parent)
curl -X GET "localhost:9200/series/_search?pretty" \
  -H "Content-Type: application/json" \
  -d  '
      {
        "query": {
          "has_parent": {
            "parent_type": "franchise",
            "query": {
              "match": {
                "title": "Star Wars"
              }
            }
          }
        }
      }
      '

## Find franchise (parent) by the film (child)!
curl -X GET "localhost:9200/series/_search?pretty" \
  -H "Content-Type: application/json" \
  -d  '
      {
        "query": {
          "has_child": {
            "type": "film",
            "query": {
              "match": {
                "title": "The Force Awakens"
              }
            }
          }
        }
      }
      '
```
