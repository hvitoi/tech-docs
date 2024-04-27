# Big data ingestion

![Big Data Ingestion](images/big-data-ingestion.png)

## Big Data

- `Volume`: TB ~ PB /day
- `Variety`: mixed data types from multiple sources
- `Velocity`: high rate

## Data Fusion

- Combine data together (similar to materialized view)
- Helps in finding `hidden patterns` and `insights` for our organizations

## Batch Processing

- Process the data stream on a fixed schedule
- E.g., for search engines, the reachable websites are indexed in batch jobs (daily web crawler) and stored in a search-optimized database
  - It's done in batch jobs because the web crawler operation takes a long time
- There is always a delay to get the real feedback from the system
  - It may cause confusion to the users
- In some other cases this simply won't work
  - E.g., event log processing must be instantaneous

## Real Time Processing

- Each new event is processed immediately from a `stream of events`
