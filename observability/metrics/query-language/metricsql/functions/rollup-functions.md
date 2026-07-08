# Rollup functions

- <https://docs.victoriametrics.com/victoriametrics/metricsql/#rollup-functions>
- aka `range functions` or `window functions`
- Apply a function to all elements of a vector

## rate

- `rate(v range-vector)`

- **Per-second average rate of increase** of the `time series` in the `range vector`

```conf
rate(v range-vector)
rate(my_time_series)[30m:]
```

## increase

- It is syntactic sugar for `rate` multiplied by the number of seconds under the specified time range window
