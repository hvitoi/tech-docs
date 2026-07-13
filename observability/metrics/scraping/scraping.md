# Metrics Scraping

- Prometheus (or VictoriaMetrics) is configured with a `target list` (via `service discovery` — k8s pod IPs, etc.) and polls the `/metrics` endpoint on each pod every `scrape_interval` (commonly 15s or 30s).
- On each scrape:
  - It records the value it read of each time series
  - Stamps it with the scrape timestamp
  - Writes `(timestamp, value)` as one new sample appended to that series' history in the TSDB

- The "raw data" of a counter is just a sequence of (time, value) snapshots taken every N seconds.

t=13:50:00 -> 10
t=13:50:15 -> 10
t=13:50:30 -> 11
t=13:50:45 -> 12

## Instrumentation

- Your app needs to be instrumented via a `client library` or by running `exporter sidecar`
- The instrumentation in your app is responsible for calculating the metric value in memory (e.g., counter, gauge) and then exposing it in the /metrics endpoint
- If the pod restarts, the in-memory counter goes back to 0

## Service Discovery

- What to scrape is usually discovered via `service discovery`
- E.g., Kubernetes, Consul, static config, etc.

## Configuration

- `Prometheus` (via remote write)
- `vmagent` (lightweight, Prometheus-compatible scraper)
