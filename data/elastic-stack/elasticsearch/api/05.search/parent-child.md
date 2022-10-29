# Parent-child search

- `franchise` is the parent, `film` is the child

```sh
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
