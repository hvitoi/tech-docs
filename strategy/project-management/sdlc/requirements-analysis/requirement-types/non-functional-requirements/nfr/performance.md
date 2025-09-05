# Performance

- Solutions
  - CDN
  - DB Indexing (partitioning and sorting)
  - API gateway caching (availability over consistency)
  - Buffering (message broker)
  - Regionally infrastructure (multi data center deployment)

## Response Time

- Also known as End-to-End latency
- Composed of the `processing time` + `waiting time`
- A common mistake is to consider the e2e latency to be only the processing time

- The metrics used is the `xth percentile`
  - It's the value below which x% of the occurrences can be found
  - E.g., 300 ms of 99% latency percentile: 99% of the requests are responded in under 300 ms
- The other portion with the worst metrics (e.g., the other 1%) is the `tail latency`
  - We want the tail latency to be as short as possible, e.g., 99% (1% tail latency)

## Throughput

- Amount of work performed by the system per unit of time
- When the throughput is so high that the system can't handle, a `performance degradation` starts whole system perform in a degraded state. This point is called `degradation point`
