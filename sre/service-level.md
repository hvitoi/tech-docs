# Service Level

- Define the metrics that matter
- Define the expected range for those metrics (what a healthy service looks like)
- Define the action to take when we can't provide the expected service

## Service Level Agreement (SLA)

- Days to accomplish something

## Service Level Indicators (SLI)

- Quantitative measure (metrics!) of some aspect
- Data is collected over a measurement window and turned into a rate, average, percentile
- E.g.
  - `request latency`
  - `error rate`
  - `system throughput`
  - `availability`/`yield`: well formed requested that succeeded. (99.95%: 3 nines and a half)

## Service Level Objectives (SLO)

- Numeric thresholds to define acceptable levels for the SLIs
- E.g.,
  - `p99 latency < 200ms for 5 min`
