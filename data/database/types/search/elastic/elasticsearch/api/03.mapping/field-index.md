# Mapping field index

- Whether the field is indexed for full-text search (analyzed) or not (not_analyzed)

```json
{
  "mappings": {
    "properties": {
      "genre": {
        "index": "not_analyzed" // field index
      }
    }
  }
}
```
