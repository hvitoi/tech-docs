# Failover

- Failover is automatic. If the primary's liveness probe fails, the operator promotes the replica with the `least replication lag`, then re-points the `-rw Service` to it. The `spec.failoverDelay` configures its sensitivity.
