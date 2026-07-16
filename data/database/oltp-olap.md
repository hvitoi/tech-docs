# Database Systems

## OLTP (Online Transaction Processing)

- **Transactional Environments** (or production environment) are systems designed for managing and processing transaction data
- They are optimized for `fast query processing` and are used for tasks like inserting, updating, and deleting records
- The data in OLTP systems is usually `up-to-date`, as users interact with it in real-time.
- Require ACID compliance to ensure data integrity and reliability during transactions
- Tend to be highly `normalized` to eliminate data redundancy
- OLTP systems often rely on `indexes` to speed up read and write operations for frequent transactions

## OLAP (Online Analytical Processing)

- **Analytical Environments** are systems designed for complex querying and analytical processing on large volumes of historical data
- These systems are optimized for `read-heavy workloads` and are often used for `business intelligence (BI)`, `data mining`, `reporting`, and `decision-making` purposes
- OLAP systems are typically used for tasks like running complex queries to analyze trends, patterns, and aggregating large amounts of data

- **Features**
  - `Analytical Workloads`: handle complex queries that involve large datasets and require aggregation, summing, and multi-dimensional analysis
  - `Data Warehousing`: OLAP systems are often used in data warehouses where large amounts of historical data from multiple sources are stored and processed.
  - `Read-heavy Queries`: These systems are optimized for read-heavy workloads, where users run queries that may involve large table scans, grouping, and aggregating data across many records.
  - `Multidimensional Data Analysis`: OLAP typically involves querying data across different dimensions (e.g., time, region, product), allowing businesses to analyze data in a flexible and interactive way

- **Types**
  - `ROLAP (Relational OLAP)`: Uses relational databases to store data and generate multidimensional views dynamically using SQL queries
  - `MOLAP (Multidimensional OLAP)`: Stores data in a multidimensional cube format, optimized for quick aggregation and complex queries. Examples include Microsoft Analysis Services.
  - `HOLAP (Hybrid OLAP)`: Combines ROLAP and MOLAP features, providing a balance between relational and multidimensional storage.

- OLAP systems are typically `denormalized` (e.g., star schema or snowflake schema) to improve query performance by reducing the need for joins during complex queries.

## Hybrid Systems

- Some modern systems, such as `HTAP` (Hybrid Transactional/Analytical Processing) databases aim to combine the capabilities of both OLTP and OLAP, allowing real-time analytics on transactional data
- Examples
  - Google Spanner
  - Microsoft Azure Synapse
  - Amazon Redshift Spectrum
