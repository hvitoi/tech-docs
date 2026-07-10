# Recording rules

- Aka `derived time series`
- A recording rule `precomputes a query on a schedule and saves the result` as a brand-new time series
- Usually done over expensive or frequently-used

## Rules file

- You define them in a rules file, evaluated on an interval (e.g. every 60s)

```yaml
groups:
  - name: http_slo
    interval: 60s
    rules:
      - record: job:http_request_errors:rate5m
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m])) by (job)
          /
          sum(rate(http_requests_total[5m])) by (job)
```

- A new series `job:http_request_errors:rate5m{job="checkout"}` is created in TSDB and it's updated every 60s
