# cat

- Catalog

```shell
# Get catalogs
curl -X GET 'localhost:9200/_cat'

# Get indicies
curl -X GET 'localhost:9200/_cat/indices?v' # v for verbose

# Get nodes
curl -X GET 'localhost:9200/_cat/nodes?v'

# Cluster health
curl -X GET 'localhost:9200/_cat/health?v'
```
