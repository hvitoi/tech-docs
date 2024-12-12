# Metric types

## Counter

- Cumulative metric
- Value can reset to zero
- Cannot decrease

## Gauge

- Single numerical value
- Can go up and down
- E.g., temperature, memory usage

## Histogram

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

## Summary

- Similar to to histogram
