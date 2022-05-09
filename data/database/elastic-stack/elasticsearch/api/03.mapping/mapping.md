# Mapping

- `Mapping` is a schema definition
  - `Explicit Mapping`: fields and their types are predefined
  - `Dynamic Mapping`: fields and their types are automatically defined by ES
- The limit number of fields is 1000

## Sample mapping

```json
{
  "mappings": {
    "properties": {
      "timestamp": { "type": "date" },
      "service": { "type": "keyword" },
      "host_ip": { "type": "ip" },
      "port": { "type": "integer" },
      "message": { "type": "text" },
      "others": {
        "type": "text",
        "fields": {
          "raw": { "type": "keyword" }
        }
      }
    }
  }
}
```
