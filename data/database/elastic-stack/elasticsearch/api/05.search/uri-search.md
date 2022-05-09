# Broad search

```shell
# Retrieve all data from an index
curl -s -X GET "localhost:9200/movies/_search" | jq .
```

## URI search

- The `score` determines how good that hit is
- Matches with best score come first
- `partial` or `full` matches are specified in the schema on field type (text or keyword)
- Query lite search can be a security issue
  - Never use in production
  - It's handy just for quick experimenting
- It must be URL encoded if used on browsers

```shell
# Simple keyword
curl -X GET "localhost:9200/movies/_search?q=Star"

# Field
curl -X GET "localhost:9200/movies/_search?q=title:star"

# AND
curl -X GET "localhost:9200/movies/_search?q=year>2010+title:trek" # year>2010 AND title:trek

# Pagination
curl -X GET "localhost:9200/movies/_search?size=2&from=2"

# Sorting
curl -X GET "localhost:9200/movies/_search?sort=title.raw" # Sort only by not_analyzed fields
```
