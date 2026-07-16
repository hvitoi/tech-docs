# Update document

- In ES, documents are immutable
- But every document maintains a `_version` field
- A updated document is a copy of the document with the `incremented_version` number
- The old documents get marked for deletion

- POST WITH `_update` will only update the changed fields. If not changes are made, the document is not udpated

```shell
curl -X POST "localhost:9200/movies/_doc/109487/_update" \
  -H "Content-Type: application/json" \
  -d  '
      {
        "doc": {
          "title": "Interstellar bare"
        }
      }
      '
```
