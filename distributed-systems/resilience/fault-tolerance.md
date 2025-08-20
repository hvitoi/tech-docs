# Fault Tolerance

- Enables the system to remain operational despite failure within one or multiple of its components

## Failure prevention

### Replication & Redundancy

- **Active-Active architecture**
  - Multiple database replicas actively receive workload
  - The multiple database sync between each other
  - If a database replica goes down, the others same its load
  - `Pros`: load is distributed. `Cons`: synchronization is very complex
- **Active-Passive architecture**
  - One primary (master/leader) replica that receives all the workload and multiple passive/follower replicas
  - The other passive replicas take periodic snapshots of the master replica
  - `Pros`: implementation is easier with snapshots. `Cons`: won't distribute the load

## Failure detection & isolation

- An auxiliary `Monitoring Service` that checks the health of the instances by:
  1. Sending periodic `health-check` requests to the services
  1. Receiving period `heart-beat` requests from the services
- Whenever an unhealthy service is detected it is then cut off from the user facing

- The monitoring service can be even more smart by:
  1. Monitoring the `error rate` in the hosts
  1. Monitoring the `response time` on the hosts
... and detect if it's in an unhealthy state

## Recovery

- Mitigation
  1. Cut off traffic to the unhealthy host
  1. Rollback to a previous code version
  1. Rollback to a previous database state
- Processes
  - Automatic `alerts` to engineers
  - Predefined `handbooks/playbooks` on what to do in certain situations
- Mechanisms
  - Automatic failovers, restarts, rollbacks, auto-scaling policies
