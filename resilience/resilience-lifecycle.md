# Resilience Lifecycle

- Set Objectives -> Design & Implement -> Evaluate & test -> Operate -> Respond & learn

## Failure Modes

- Gray failures
- Database corruption
- Overload

- Solutions
  - Multi Regions, Multi AZ, Backups

## High Availability

- Have the app running in which you don't have a single point of failure

## Disaster Recovery

- RPO / RTO
- Create bounded recovery times, recover fast!

## Resilience Properties

- Fault isolation
- Sufficient capacity
- Timely output
- Correct output
- Redundancy

## Categories of failures (SEEMS)

- `Single points of failure`
- `Excessive load`
- `Excessive latency`
- `Misconfiguration and bugs`
- `Shared fate`: violating intended fault isolation

## FMEA? GMUD?

## Resilience Trade-offs

- Cost & effort
- Complexity
- Operational burden
- Consistency & latency
