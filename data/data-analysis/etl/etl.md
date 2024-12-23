# ETL (Extract, Transform, Load)

- Move data `from OLTP into OLAP` systems
- It's a system that `extracts` the unstructured data from the production databases, `transforms` the data into structure and meaningful data and `loads` the data into an analytical environment

- **Extract**
  - Get the raw data (database log files), divide it in small batches of subtasks and then process each batch in parallel

- **Transform**
  - Transforms the data as we want

- **Load**
  - Loads the data into analytical environments
    - Data Warehouse (Google Big Query)
    - Databricks

## Workflow

### Data Ingestion

- Collects data from the transactional environment

### Data Processing

- Processes the collected raw data and outputs data that can be used for analyses

### Data Serving

- Propagates the computed data to `BI tools` analytical environments (such as Looker, Google Data Studio) and to the production environment

### Data Access

- All the data that was transformed and stored can be accessed through various BI tools

### Data Governance

- Implementing granular access control of data in the analytical environments
- Managing PII data inventory and data subject rights

## Batch vs. Stream Processing

- The data is processed in two ways
  - **Batch processing system** (historical data)
  - **Stream processing system** (real-time data)

### Batch Processing System

- The data is available in the analytical environment `within 1 day`

### Stream Processing System

- It's required by systems that need fresh data, often some kind of monitoring (e.g., fraud, product rollout, operational)
- The data is available in the analytical environment `within an hour`
