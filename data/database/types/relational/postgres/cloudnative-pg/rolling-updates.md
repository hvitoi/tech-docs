# Rolling Updates

- Most config changes are applied as a rolling update: `replicas are updated first`, then a switchover moves the primary role to an already-updated instance, then the old primary is updated. Controlled by:
