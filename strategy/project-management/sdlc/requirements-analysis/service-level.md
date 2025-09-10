# Service Level

- Define the metrics that matter
- Define the expected range for those metrics (what a healthy service looks like)
- Define the action to take when we can't provide the expected service

## Service Level Agreement (SLA)

- An agreement between the `service provider` and the `clients/users`
- A legal contract that represents quality of the service. With explicit penalties and financial consequences
- E.g.,
  - Availability
  - Performance
  - Data durability
  - Time to respond to system failures
- SLAs are common for external paying users (always), free external users (sometimes) and internal users (occasionally)

## Service Level Indicators (SLI)

- Quantitative measure (metrics!) of some aspect
- Data is collected over a measurement window and turned into a rate, average, percentile
- Quantitative measure of the compliance with a SLO
- The actual numbers, metrics measured by monitoring a service
- SLOs rely on the SLIs to measure if the goal is achieved or not

- E.g.
  - `request latency`
  - `error rate`
  - `system throughput`
  - `availability`/`yield`: well formed requested that succeeded. (99.95%: 3 nines and a half)

## Service Level Objectives (SLO)

- Numeric thresholds to define acceptable levels for the SLIs
- Individual goals set for the system
- Each SLO represents a target value/range that the system needs to meet
- The quality attributes from the beginning of the design process will make their way to one or more SLOs
- If a system has an SLA, it will be detailed as multiple SLOs aggregated in a single legal document

- E.g.,
  - `p99 latency < 200ms for 5 min`
  - Availability of 3 nines
  - Response time of 100 ms for 90th percentile
