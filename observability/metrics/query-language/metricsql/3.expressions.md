# Expressions

```metricsql
<expression> := <metric_name>{<label_selectors>} <operator> <aggregation/functions>
```

## Instant vector

- A `set of time series` containing a `single sample for each time series`, all sharing the `same timestamp`

```conf
ALERTS{raw_name="service_is_underprovisioned"}
```

```json
[
  {
    "metric": {
      "__name__": "ALERTS",
      "alertgroup": "my_alert_group",
      "alertname": "service_is_underprovisioned_460ad1f283a661468925b95e00221d0f60de7416",
      "alertstate": "firing",
      "raw_name": "service_is_underprovisioned"
    },
    "value": [
      1757431857.472,
      "1"
    ],
    "group": 1
  }
]
```

## Range vector

- A `set of time series` containing a `range of data points over a time for each time series`

```conf
ALERTS{raw_name="service_is_underprovisioned"}[5m]
```

```json
[
  {
    "metric": {
      "__name__": "ALERTS",
      "alertgroup": "my_alert_group",
      "alertname": "service_is_underprovisioned_460ad1f283a661468925b95e00221d0f60de7416",
      "alertstate": "firing",
      "raw_name": "service_is_underprovisioned"
    },
    "values": [
      [1757431650, "1"],
      [1757431680, "1"],
      [1757431710, "1"],
      [1757431740, "1"],
      [1757431770, "1"],
      [1757431800, "1"],
      [1757431830, "1"],
      [1757431860, "1"]
    ],
    "group": 1
  }
]
```

```conf
# Time Duration

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

## Scalar

- **Float literals**
- A single floating point number (no labels)

```conf
23
-2.43
3.4e-9
0x8f
-Inf
NaN
```

## String

- **String literal**
- Used in limited string-processing functions like label_replace()
- Defined with quotes, double quotes or backticks

```conf
"this is a string"
'these are unescaped: \n \\ \t'
`these are not unescaped: \n ' " \t`
```
