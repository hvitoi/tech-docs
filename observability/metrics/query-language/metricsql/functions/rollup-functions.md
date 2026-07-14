# Rollup functions

- <https://docs.victoriametrics.com/victoriametrics/metricsql/#rollup-functions>
- aka `range functions` or `window functions`
- Rollup functions always operate on a `range vector`

## rate(series_selector[d])

> Applied to counters only

- Average `per-second rate` (increase/decrease) over the given lookbehind window d per each time series returned from the given series_selector
- The lookbehind window (d=1m) tells what window of samples it will use to calculate the per-second rate
- Higher d smooths the graph, while lower d brings more noise to the graph

```conf
rate(http_requests_total{job="api-server"}[1m])
```

$$(Vcurr-Vprev) / (Tcurr-Tprev)$$

where:
$Vcurr$: value at the current point $Tcurr$
$Vprev$: value at the point $Tprev=Tcurr-d$

## increase(series_selector[d])

- It is syntactic sugar for `rate` multiplied by the number of seconds under the specified time range window

## min_over_time(series_selector[d])

> Applied to gauge only

```conf
min_over_time(node_memory_MemFree_bytes[5m])
```

## Especial Cases

### Omission of lookbehind window [d]

- On **MetricQL** (Vicmetrics), the `[d]` lookbehind can be omitted
- The lookbehind window is automatically selected based on the `step` param passed to `/api/v1/query_range` and the real interval between raw samples (aka scrape_interval)
- E.g., `rate(http_requests_total)` is valid, no need to `rate(http_requests_total)[5m]`

### default_rollup

- A bare selector is auto-wrapped in `default_rollup` function in `range queries`
- `foo{bar="baz"}` becomes `default_rollup(foo{bar="baz"}[<auto window>])`
