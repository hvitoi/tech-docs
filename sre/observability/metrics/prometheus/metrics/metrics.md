# Metrics

- Prometheus collects and stores its metrics as `time series data`, i.e. metrics information is stored with the `timestamp` at which it was recorded, alongside optional key-value pairs called `labels`

## Attributes

- Each metric has `type` and `help` attributes
  - `Help`: description of what the metrics is
  - `Type`: there are three types
    - _Counter_: How many times happened
    - _Gauge_: The current value now
    - _Histogram_: how long or how big
