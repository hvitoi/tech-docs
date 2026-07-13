# Time series

- A metric is a `time series` - a stream of (timestamp, value) numbers
- Every unique combination of `name + labels` is a different time series
- Prometheus collects and stores its metrics as `time series data`, i.e. metrics information is stored with the `timestamp` at which it was recorded, alongside optional key-value pairs called `labels`

```conf
# time series name: http_requests_total
# time series labels: method="GET", status="200", service="checkout"
http_requests_total{method="GET", status="200", service="checkout"}
```

## Metric types

### Counter

- Cumulative metric (cannot decrease)
- Value can reset to zero
- You never read the raw value; you compute its rate: `rate(http_requests_total[5m]` = requests/sec).

```conf
http_requests_total{method="GET", status="200", service="checkout"}
```

### Gauge

- Single numerical value
- Can go up and down
- E.g., temperature, memory usage

```conf
memory_bytes
```

### Histogram

- Sample observations
- Histogram is cumulative
- E.g., request durations, response sizes
- An histogram generates 3 metrics
  - `<metric_name>_sum`
  - `<metric_name>_count`
  - `<metric_name>_bucket`: the number of measurement lower or equal to the value specified for each bucket. An `+Inf` bucket is automatically defined.

```conf
my_metric_bucket{le="1080"} # number of measurements lower or equal to 1080
my_metric_bucket{le="+Inf"} # total number of measurements (no upper bound)

my_metric_count # total number of measurements (always the same as my_metric_bucket{le="+Inf"})
my_metric_sum # sum of all measurements (the raw measurement value, not the highest fitted bucket)
```

### Summary

- Similar to histogram, but percentiles are precomputed client-side (less flexible, histograms are usually preferred)
