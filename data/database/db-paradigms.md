# Database Paradigms

- <https://db-engines.com/en/ranking_trend>
- <https://db-engines.com/en/ranking>

## Relational DB

- Rigid structure enforced by table's `schema`
- Has support for `transactions` (ACID compliant)
- Difficult to scale
- Slower read operations
- On-line Transaction Processing (OLTP)

- **Implementations**
  - MySQL
  - Postgres
  - SQL Server
  - RDS & Aurora (AWS)

## Key-Value DB

- It's a large scale hash table
- Data stored in RAM
- Perfect use-case for caches and counters

- **Implementations**
  - Redis
  - Memcached
  - Etcd

## Document Oriented DB

- Each document is a container for key-value pairs
- No schema
- Documents are grouped together in collections

- **Implementations**
  - MongoDB
  - Firestore
  - DynamoDB
  - CouchDB

## Graph DB

- Data is represented as `nodes` (circles/vertexes)
- Relationships are represented as `edges` (arrows)
- Edges can also be weighted

- Operations
  - Link
  - Traverse
  - Analyze

- Pros
  - Good for n:n relationships!
  - Good for fraud detection in finance and recomendation systems
  - Good for recommendation engines

- **Implementations**
  - Neo4j
  - DGraph
  - AWS Neptune

## Wide-Column DB

- Keys store multiple columns (values)
- No schema
- Good for time-series data, historical records, high-write, low-read

- **Implementations**
  - Cassandra
  - HBase

## Search DB

- Similar to document-oriented DBs
- Search DB analyze all the text in the document and create index of the searchable terms
- Good for type-ahead search bars

- **Implementations**
  - Lucene
  - Solr
  - ElasticSearch
  - Algolia
  - MeiliSearch

## Multi Model DB

- **Implementations**
  - Fauna: describe how to access the data with GraphQL
