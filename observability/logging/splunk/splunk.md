# Splunk

- Send data to Splunk and then they send back analysis about:
  - Application Delivery
  - IT Operations
  - Security, Compliance and Fraud
  - Business Analytics
  - Industrial Data and IoT
- Splunk `aggregates logs` - all kinds of logs! And make them `accessible`
- Prometheus vs. Splunk
  - Prometheus: metrics, service health, observability
  - Splunk: unstructured data (usually logs)

## Pipeline

1. Collect Data
1. Index Data
1. Search & Explore
1. Alert & Action
1. Enrich Data
1. Report & Visualize
1. Analyze & Predict

## Components

- **Forwarders**
  - Listen logs and send to the indexers
  - It's a sidecar!
  - Application logs: use a lib to log into `application.log` file
  - Kubernetes logs: it's sent by `fluentd`
  - AWS logs: it's sent by S3 Events & Lambda
- **Indexers**
  - Search peers
  - Index and parse the data
  - It's a cluster with N indexers (managed by splunk)
- **Search head**
  - User interface to search the and fetch data
  - It's expandable with plugins
  - It's a cluster with N search heads (managed by splunk)

## Search Head

- `Search & Reporting`: big search box. Uses `SPL` language. Alerts can be created from here too
- `Splunk Machine Learning Toolkit`: predictions and models, detect outliers
- `ES Content Updates`: dashboards & alerts
