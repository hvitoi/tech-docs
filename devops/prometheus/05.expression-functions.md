# Functions

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

## Others

- abs()
- absent()
- absent_over_time()
- ceil()
- changes()
- clamp()
- clamp_max()
- clamp_min()
- day_of_month()
- day_of_week()
- day_of_year()
- days_in_month()
- delta()
- deriv()
- exp()
- floor()
- histogram_quantile()
- holt_winters()
- hour()
- idelta()
- increase()
- irate()
- label_join()
- label_replace()
- ln()
- log2()
- log10()
- minute()
- month()
- predict_linear()
- resets()
- round()
- scalar()
- sgn()
- sort()
- sort_desc()
- sqrt()
- time()
- timestamp()
- vector()
- year()
- "aggregation"\_over_time()
- Trigonometric Functions
