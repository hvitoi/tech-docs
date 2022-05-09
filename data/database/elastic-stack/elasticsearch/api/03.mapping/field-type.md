# Mapping field types

- `string`:
- `long`:
- `interger`: int number
- `date`: date field
- `keyword`: Allow the string to be only searched if typed exactly as is (case sensitive)
- `text`: gets analyzer applied to it (lowercase, filters, partial matches, etc)
- `join`: join data from another source
- `flattened`: designed to handle unknown or large number of inner fields
- `search_as_you_type`: for searching

```json
{
  "mappings": {
    "properties": {
      "id": {
        "type": "integer"
      },
      "year": {
        "type": "date"
      },
      "genre": {
        "type": "keyword"
      },
      "title": {
        "type": "text",
        "analyzer": "english"
      }
    }
  }
}
```
