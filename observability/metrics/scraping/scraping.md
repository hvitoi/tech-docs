# Metrics Scraping

- The action of pulling sample from the target services in the `/metrics` endpoint
- On each scrape:
  - It records the value it read of each time series
  - Stamps it with the scrape timestamp
  - Writes `[timestamp, value]` as one new sample appended to that series' history in the TSDB

- The "raw data" of a counter is just a sequence of (time, value) snapshots taken every N seconds.

t=13:50:00 -> 10
t=13:50:15 -> 10
t=13:50:30 -> 11
t=13:50:45 -> 12

## Target List & Service Discovery

- The `target list` is the list of service to pull for metric samples
- What to scrape is usually discovered via `service discovery`
- E.g., Kubernetes pod IPs, Consul, static config, etc.

## Scrape Interval

- Prometheus is configured to poll to poll the `/metrics` endpoint of each target on a fixed period
- This `scrape interval` is commonly 15s

## Instrumentation

- Your app needs to be instrumented via a `client library` or by running `exporter sidecar`
- The instrumentation in your app is responsible for calculating the metric value in memory (e.g., counter, gauge) and then exposing it in the /metrics endpoint
- If the pod restarts, the in-memory counter goes back to 0

## Configuration

- `Prometheus` (via remote write)
- `vmagent` (lightweight, Prometheus-compatible scraper)
