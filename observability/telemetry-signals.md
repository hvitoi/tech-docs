# Telemetry signals

- 3 pillars of observability
  - **Metrics**
  - **Logs**
  - **Traces**

## Metrics

- Metrics are `numeric representation of data` measured over intervals of time
- A `threshold` is an objetive that should not be trespassed
- Ideally the current `state` must not reach the threshold

- 4 golden signals
  - `latency`: time to serve a request
  - `traffic`: requests/s
  - `error`: error rate of requests
  - `saturation`: fullness of a service

- Common metrics
  - CPU, Memory, Disk Usage

## Logging

- Log is a `immutable`, `timestamped` record of `discrete events` that happened over time

## Tracing

- Trace is a representation of a series of causally related distributed events
- Shows the `end-to-end request flow` through a distributed system
