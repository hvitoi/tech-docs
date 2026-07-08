# Metrics System

- A metrics system is composed of
  - A TSDB
  - A scraper
  - A query language

## Common setup

1. `Prometheus` (scrapes targets, pushes to VictoriaMetrics via remote_write, and handle alerting)
1. `VictoriaMetrics` (stores time series efficiently)
1. `Grafana` (queries VictoriaMetrics)
