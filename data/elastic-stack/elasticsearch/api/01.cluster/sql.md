# Elasticsearch SQL

- Added in Elasticseach 6.3

1. SQL query
1. Unresolved AST
1. Resolved plan
1. Optimized plan
1. Physical plan
1. Results

- `indexes` turn into `tables`
- `documents` turn into `rows`

```sh
curl -s "localhost:9200/_sql?format=txt" \
  --request GET \
  --header "Content-Type: application/json" \
  --data @sql.json
```

```json
{
  "query": "DESCRIBE movies"
}
```

```json
{
  "query": "SELECT title FROM movies LIMIT 10"
}
```

```json
{
  "query": "SELECT title, year FROM movies WHERE year < 1920 ORDER BY year"
}
```

## Translate sql to conventional json query

```sh
curl -s "localhost:9200/_sql/translate" \
  --request GET \
  --header "Content-Type: application/json" \
  --data @sql.json \
| jq .
```

## Elasticsearch SQL CLI

- `/usr/share/elasticsearch/bin/elasticsearch-sql-cli`
