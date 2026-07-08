# Metrics Scraping

- Scraping works by periodically sending HTTP requests to specific endpoints on the `target systems` (called targets) to collect metrics. This process is called `scraping`
- Conventionally the endpoint on the target systems is `/metrics` (e.g., `karpenter.kube-system.svc.cluster.local:8080/metrics`)

## Prometheus text-based exposition format

- These metrics/time-series are exposed in the `/metrics` endpoints in the `Prometheus text-based exposition format`

```conf
# what /metrics looks like — plain text
http_requests_total{method="GET",status="200"} 1027
http_requests_total{method="GET",status="500"} 3
process_resident_memory_bytes 4.1287680e+07
```

- Prometheus sends an HTTP GET request to the `/metrics` endpoint of each target at the specified interval

## Configuration

- `Prometheus` (via remote write)
- `vmagent` (lightweight, Prometheus-compatible scraper)
