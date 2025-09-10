# Availability

$$Availability = \frac{Uptime}{Uptime+Downtime}$$

> Fault Tolerance is a way to achieve a higher availability despite failures

- `MTBF`: Mean Time Between Failures
  - Average time the system is operational
  - Because the uptime
- `MTTR`: Mean Time to Recovery
  - Average time to detect and recover from a failure
  - Basically the downtime

$$Availability = \frac{MTBF}{MTBF+MTTR}$$

| Availability    | Daily Downtime | Weekly Downtime | Monthly Downtime |
| -               | -              | -               | -                |
| 99%  (2 nines)  | 14 min 25 s    | 1 h 40 min      | 7 h 18 m         |
| 99.9% (3 nines) | 1 min 26 s     | 43 m 12 s       | 8 h 45 min       |

## Causes

- `Human Error`: faulty code
- `Software Errors`: long garbage collections, out-of-memory exceptions
- `Hardware Failures`: network failures, servers, routers, power outages

## Solutions

- Database replication and redundancy (durability)
- Failover to other region
- Availability over Consistency (AP over CP)
- Snapshots & Backups
- Postmortems
