# Rollup functions

- <https://docs.victoriametrics.com/victoriametrics/metricsql/#rollup-functions>
- aka `range functions` or `window functions`
- Apply a function to all elements of a vector

## rate(v range-vector)

- Per-second average rate of increase of the `time series` in the `range vector`

```conf
rate(http_requests_total{job="api-server"}[5m])
```

## increase

- It is syntactic sugar for `rate` multiplied by the number of seconds under the specified time range window
