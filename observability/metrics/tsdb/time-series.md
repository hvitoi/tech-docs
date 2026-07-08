# Metrics

- A metric is a `time series` - a stream of (timestamp, value) numbers

```conf
# name: http_requests_total
# labels: {method="GET", status="200", service="checkout"}
http_requests_total{method="GET", status="200", service="checkout"}
→  [ (t1, 5), (t2, 9), (t3, 14), ... ]
```

- Every unique combination of `name + labels` are different time series

-

- Prometheus collects and stores its metrics as `time series data`, i.e. metrics information is stored with the `timestamp` at which it was recorded, alongside optional key-value pairs called `labels`

## Attributes

- Each metric has `type` and `help` attributes
  - `Help`: description of what the metrics is
  - `Type`: there are three types
    - _Counter_: How many times happened
    - _Gauge_: The current value now
    - _Histogram_: how long or how big

## Examples

```shell
ALERTS{alertname=~"service_is_down.*", service=~".*"}
```

- Percentiles: p90, p95, p99
- Trimmed mean: tm90, tm95, tm99
