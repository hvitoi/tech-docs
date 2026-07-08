# Time Series Selectors

- Pick a selection from a a time series
- Uses the metric name as a function
- `Label matching operators`
  - `=`: Select labels that are exactly equal to the provided string.
  - `!=`: Select labels that are not equal to the provided string.
  - `=~`: Select labels that regex-match the provided string. env=~"foo" is treated as env=~"^foo$".
  - `!~`: Select labels that do not regex-match the provided string.

```conf
# all the time series
http_requests_total

# filter the time series
http_requests_total{job="prometheus", group="canary"}

# filter with regex
http_requests_total{environment=~"staging|testing|development", method!="GET"}
http_requests_total{environment=~"$ENVS"} # from list variable
http_requests_total{status!~"4.."}

# the time series to be used can be picked by a regex
{__name__=~"http_requests_total.*"}

# Also work for range vectors (selects a range of samples)
http_requests_total{job="prometheus"}[5m]
```

## Offset Modifier

- Changes the time offset for an instant

```conf
# request with the instant time past 1 week
http_requests_total{method="GET"} offset 1w
rate(http_requests_total[5m] offset 1w)
```

### @ Modifier

- Specify the instant time

```conf
http_requests_total @ 1609746000
sum(http_requests_total{method="GET"} @ 1609746000)

# offset after @
http_requests_total @ 1609746000 offset 5m
# offset before @
http_requests_total offset 5m @ 1609746000
```
