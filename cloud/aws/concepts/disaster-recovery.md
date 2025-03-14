# Disaster Recovery

- `Disaster` is a negative impact on `business continuity` or `finance`
- `Disaster Recovery` (DR) is preparing recover from a disaster

## RPO & RTO

- `Recovery Point Objective` (RPO)
- `Recovery Time Objective` (RTO)

![RPO & RTO](.images/dr-rpo-rto.png)

## DR Strategies

1. `Backup & Restore`
1. `Pilot Light`
1. `Warm Standby`
1. `Hot Site / Multi Site`

![DR Strategies](.images/dr-strategies.png)

### Backup & Restore

- High RPO
- High RTO

![Backup & Restore](.images/dr-backup-restore.png)

### Pilot Light

- A small version of the system is always running in the cloud for a fast `failover`
- Faster recovery

![Pilot Light](.images/dr-pilot-light.png)

### Warm Standby

- Full system is running in the cloud for even faster `failover`

![Warm Standby](.images/dr-warm-standby.png)

### Multi-Site / Hot-Site

- Full production scale running on the cloud and on-premise

![Multi-Site / Hot-Site](.images/dr-multi-site.png)
