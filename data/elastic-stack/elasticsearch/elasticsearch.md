# Elasticsearch

- Elasticsearch is a `Analytics` & `Full-text search engine`
- Analyze `application logs` and `system metrics`: `Application Performance Management` (APM)
- Forecasting

## Elastic Stack

- `Kibana`: Analytics & visualization platform. It's a dashboard, a web interface to the data in ES. Often used for log analysis
- `Logstash`: Data processing pipeline. It's a way to feed data into ES
- `X-Pack`: Security, monitoring, alerting,reporting, machine learning, graph exploration, elasticSQL
- `Beats`:
  - Filebeat: search logs to logstash
  - Metricbeat: system level, cpu, memory
  - Packetbeat: ...

## Elasticsearch logical concepts

### Document

- `Document` is a record of data. It's stored in JSON format
- The `schema` for the document is the definition of what sort of information is stored. It's stored in the index

### Index

- The `index` is where the documents are stored. It aggregates similar data. E.g., movies, ratings, users
- In the index is defined the individual `fields` and what data type they accept

### Inverted index

- Map each word to the documents where it appear
- They quickly map search terms to documents

- `Document 1`: Space: The final frontier. These are the voyages...
- `Document 2`: He's bad, he's number one. He's the space cowboy with the laser gun!

| Word     | Occurrence |
| -------- | ---------- |
| space    | 1,2        |
| the      | 1,2        |
| final    | 1          |
| frontier | 1          |
| he       | 2          |
| bad      | 2          |

### Term Frequency (TF) & Inverse Document Frequency (IDF)

- **Term Frequency**: How often a term appear in a `given` document
- **Document Frequency**: How often a term appear in `all` documents
- **Term Frequency**/**Document Frequency**: Measures the `relevance` of the term in a document

- `TF*IDF`: multiplication of both values

## Elasticsearch Scaling

- A index is hashed into `shards`. One `primary` shard and optionally `replica` shards

### Shards

- A `shard` is a self-contained instance of Lucene
- Shards can be located across different nodes in a cluster

- `Primary shard`:
  - Receive read and write requests.
  - Replicate the shards.
  - If a primary shard fails, ES will elect another replica to be the new primary shard
  - The number of primary shards cannot be changed later (if you do not want to re-index everything)
- `Replica shard`:
  - Receive only read requests
  - Adding more replica shards increases the read throughput
