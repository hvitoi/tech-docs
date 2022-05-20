# Apache Spark

- Engine for processing large-scale data (faster alternative to mapreduce)
- Uses `DAG Engine` (directed acyclic graph) to optimize the workflow, like pig on tez
- Can be coded in `python`, `java` or `scala` (preferred)
- It has a huge ecosystem on top of it for ML, AI, BI, etc
- Spark does not need to run on Hadoop, it can run on its own

## Resilient Distributed Dataset (RDD)

- Spark saves data in memory on RDD (`Resilient Distributed Dataset`)
- Spark tries to keep as much as possible on RAM (not on RDFS)
- Up to 100x faster than mapreduce

## Scalability

- `Driver Program`: Spark Context
- `Cluster Manager`: Spark or Yarn
- `Executor`: Cache, Tasks

## Components

- `Spark Core`
- `Spark Streaming`: ingest data as it's being produced
- `Spark SQL`: SQL interface to spark
- `MLLib`: Machine Learning and Data Mining
- `GraphX`: Graphs handling
