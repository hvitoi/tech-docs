# Exposition Formats

## Text-based format

```conf
# HELP http_requests_total The total number of HTTP requests
# TYPE http_requests_total counter
http_requests_total{method="GET",code="200"} 1027
http_requests_total{method="GET",code="404"} 3

# HELP cpu_usage_seconds_total Total CPU time consumed
# TYPE cpu_usage_seconds_total counter
cpu_usage_seconds_total 12345.67

# HELP memory_usage_bytes Current memory usage in bytes
# TYPE memory_usage_bytes gauge
memory_usage_bytes 654321

# HELP go_threads Number of OS threads created
# TYPE go_threads gauge
go_threads 12

# HELP application_up Whether the application is up and running (1 for up, 0 for down)
# TYPE application_up gauge
application_up 1

# HELP db_query_duration_seconds Histogram of database query durations
# TYPE db_query_duration_seconds histogram
db_query_duration_seconds_bucket{le="0.01"} 25
db_query_duration_seconds_bucket{le="0.05"} 50
db_query_duration_seconds_bucket{le="0.1"} 75
db_query_duration_seconds_bucket{le="0.5"} 100
db_query_duration_seconds_bucket{le="1"} 110
db_query_duration_seconds_bucket{le="+Inf"} 120
db_query_duration_seconds_sum 35.5
db_query_duration_seconds_count 120

# HELP custom_metric Example of a custom metric
# TYPE custom_metric counter
custom_metric{label1="value1",label2="value2"} 42
```

## Annotations

- **HELP annotation**: Provide a human-readable description of the metric

- **TYPE annotation**: Indicate the metric type: `counter`, `gauge`, `histogram`, or `summary`.
