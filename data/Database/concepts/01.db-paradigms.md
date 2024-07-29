# Database Paradigms

- <https://db-engines.com/en/ranking_trend>
- <https://db-engines.com/en/ranking>

## Relational DB

- Rigid structure enforced by table's `schema`
- Has support for `transactions` (**ACID** compliant)
  - `Atomicity`: The outcome of a transaction can either be completely successful or completely unsuccessful. The whole transaction must be rolled back if one part of it fails.
  - `Consistency`: Transactions maintain integrity restrictions by moving the database from one valid state to another valid state. The transaction cannot violate predefined rules or else it will fail.
  - `Isolation`: Concurrent transactions are isolated from one another, assuring the accuracy of the data. On modern rdbms it has lock-by-row mechanisms
  - `Durability`: Once a transaction is committed, its modifications remain in effect even in the event of a system failure.
- Difficult to scale
- Slower read operations
- On-line Transaction Processing (OLTP)

- Implementations
  - MySQL
  - Postgres
  - SQL Server
  - RDS & Aurora (AWS)

## Key-Value DB

- It's a large scale hash table
- Data stored in RAM
- Perfect use-case for caches and counters

- Implementations
  - Redis
  - Memcached
  - Etcd

## Document Oriented DB

- Each document is a container for key-value pairs
- No schema
- Documents are grouped together in collections

- Implementations
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

- Implementations
  - Neo4j
  - DGraph
  - AWS Neptune

## Wide-Column DB

- Keys store multiple columns (values)
- No schema
- Good for time-series data, historical records, high-write, low-read

- Implementations
  - Cassandra
  - HBase

## Search DB

- Similar to document-oriented DBs
- Search DB analyze all the text in the document and create index of the searchable terms
- Good for type-ahead search bars

- Implementations
  - Lucene
  - Solr
  - ElasticSearch
  - Algolia
  - MeiliSearch

## Multi Model DB

- Implementations
  - Fauna: describe how to access the data with GraphQL
