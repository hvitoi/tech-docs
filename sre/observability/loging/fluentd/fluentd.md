# Fluentd

> A log collector (not metrics)

- **Purpose**: A data collector used to aggregate and transport `log data`.

- **Focus**: Logs and unstructured/semi-structured data (e.g., application logs, system logs).

- **Use Case**: Collects logs from multiple sources, processes or transforms them, and sends them to various destinations like Elasticsearch, Kafka, or S3.

## Kubernetes

- On Kubernetes it runs as a DaemonSet
- Collects the logs from the Pods and push it to anywhere (e.g., AWS CloudWatch)
