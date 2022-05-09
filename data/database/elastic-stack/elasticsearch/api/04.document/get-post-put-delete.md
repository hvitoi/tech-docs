# Insert document into index

- GET to `_doc` retrieves a document from the index
- POST to `_doc` inserts a new document (auto generated ID)
- PUT to `_doc` inserts a new document (specify ID)
- DELETE to `_doc` deletes a document

## GET document

```shell
curl -X GET "localhost:9200/movies/_doc/109487"
```

## POST document

- Auto-generated ID: `xH_UtnYB5ac5TgxH2ksQ`

```shell
curl -s "localhost:9200/movies/_doc" \
  --request POST \
  --header "Content-Type: application/json" \
  --data @document.json \
| jq .
```

```json
{
  "genre": ["IMAX", "Sci-Fi"],
  "title": "Interstellar",
  "year": 2014
}
```

## PUT document

- Specified ID: `109487`
- If the ID already exists, the document will be replaced entirely

```shell
curl -X PUT "localhost:9200/movies/_doc/109487" \
  --header "Content-Type: application/json" \
  --data @document.json
```

```json
{
  "genre": ["IMAX", "Sci-Fi"],
  "title": "Interstellar",
  "year": 2014
}
```

## DELETE document

```shell
# First get the doc to see if it's the correct doc to be deleted
curl -X GET "localhost:9200/movies/_search?q=Dark"
curl -X GET "localhost:9200/movies/_doc/58559"

# Delete document
curl -X DELETE "localhost:9200/movies/_doc/58559"
```
