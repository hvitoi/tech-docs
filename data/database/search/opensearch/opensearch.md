# OpenSearch

- Open-source fork of Elasticsearch, maintained by AWS since 2021
- Fully compatible with Elasticsearch 7.10 API (the last open-source version)
- <https://opensearch.org/>

## Core Concepts

- **Index**: logical namespace that holds documents (equivalent to a table)
- **Document**: JSON object stored in an index
- **Shard**: unit of distribution — each index is split into shards across nodes
- **Inverted Index**: underlying data structure enabling fast full-text search (via Apache Lucene)

## Key Features

- Full-text search with relevance ranking (BM25 by default)
- Faceting, aggregations, and filtering
- Multi-tenancy via index aliases
- Built-in security (auth, TLS, RBAC) — included for free, unlike Elasticsearch
- OpenSearch Dashboards (fork of Kibana) for visualization

## k-NN Plugin (Vector Search)

- Adds Approximate Nearest Neighbor (ANN) search on top of the search engine
- Supports dense vector fields (`knn_vector` type)
- ANN algorithms: **HNSW** (default) and **IVF**
- Similarity metrics: cosine, dot product, L2 (Euclidean)
- Enables **hybrid search**: combine BM25 keyword score with vector similarity in a single query
- Use case: semantic search, RAG pipelines, recommendation engines

```json
// Index mapping with a vector field
{
  "mappings": {
    "properties": {
      "embedding": {
        "type": "knn_vector",
        "dimension": 1536,
        "method": {
          "name": "hnsw",
          "space_type": "cosinesimil"
        }
      }
    }
  }
}
```

## Opensearch vs. Elasticsearch

| Aspect           | OpenSearch             | Elasticsearch          |
| ---------------- | ---------------------- | ---------------------- |
| License          | Apache 2.0             | Elastic License (SSPL) |
| Managed offering | AWS OpenSearch Service | Elastic Cloud          |
| Security         | Included               | Paid tier              |
| Vector search    | k-NN plugin            | Built-in since 8.x     |
