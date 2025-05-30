# Data types

- Prometheus' is an `expression language`

## Expressions

- The expressions can be evaluated to
  - **Instant vector**
  - **Range vector**
  - **Scalar**
  - **String**

## Literals

- **String literal**

  - Defined with quotes, double quotes or backticks

  ```shell
  "this is a string"
  'these are unescaped: \n \\ \t'
  `these are not unescaped: \n ' " \t`
  ```

- **Float literals**

  - Literal integer or floating-point numbers

  ```shell
  23
  -2.43
  3.4e-9
  0x8f
  -Inf
  NaN
  ```

## Time Series Selectors

### Instant Vector Selectors

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
```

### Range Vector Selector

- Like instant vector, but it also select a range of samples
- Specify how far back in time the values should be fetched for each resulting range

```conf
http_requests_total{job="prometheus"}[5m]
```

### Time Duration

- Specified by a number, following by a unit

```conf
ms # milliseconds
s # seconds
m # minutes
h # hours
d # days - assuming a day has always 24h
w # weeks - assuming a week has always 7d
y # years - assuming a year has always 365d

# concatenation
1h30m
```

### Offset Modifier

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
