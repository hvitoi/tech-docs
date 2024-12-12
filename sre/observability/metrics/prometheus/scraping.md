# Metrics Scraping

- Prometheus scraping works by periodically sending HTTP requests to specific endpoints on the `target systems` (called targets) to collect metrics. This process is called `scraping`

## Targets

- Prometheus monitors the `targets`
  - Linux/Windows Server, Single Application, Apache Server, Databases, etc
- Each target has `units`, which expose the `metrics`
  - CPU, memory/disk usage, exception counts, requests count, request duration, etc

## Target Exposition and Metrics Endpoint

- Targets (e.g., applications, services, or exporters) expose metrics via an HTTP endpoint, typically in a format like `/metrics` (e.g., `karpenter.kube-system.svc.cluster.local:8080/metrics`)
- These metrics are usually in the `Prometheus text-based exposition format`

## Prometheus Configuration

- In the prometheus configuration file `prometheus.yml`, you define the `scrape job` with

```yaml
scrape_configs:
  - job_name: 'example'
    scrape_interval: 15s
    static_configs:
      - targets: ['localhost:8080']
```

- Prometheus sends an HTTP GET request to the `/metrics` endpoint of each target at the specified interval

## Time-series database

- Prometheus processes the collected metrics and stores them in its `time-series database` for querying and alerting.
- The database can be queried via `PromQL` for visualization and alerting
