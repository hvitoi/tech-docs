# Metrics Scraping

- Scraping works by periodically sending HTTP requests to specific endpoints on the `target systems` (called targets) to collect metrics at the specified interval. This process is called `scraping`
- Conventionally the endpoint on the target systems is `/metrics` (e.g., `karpenter.kube-system.svc.cluster.local:8080/metrics`) usually using a `text-based exposition format`

## Configuration

- `Prometheus` (via remote write)
- `vmagent` (lightweight, Prometheus-compatible scraper)
