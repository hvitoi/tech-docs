# PodDisruptionBudget (pdb)

> A disruption refers to an event or action that causes a Pod to become unavailable or terminate. Disruptions can be voluntary or involuntary, depending on the cause

- It's a mechanism to ensure a `minimum level of availability` for Pods during voluntary pod disruptions (deletion)
- It sets limits on how many Pods from a specific set (e.g., in a Deployment, ReplicaSet, or StatefulSet) can be unavailable at the same time due to actions like:
  - Node draining during maintenance.
  - Cluster scaling.
  - Upgrades initiated by administrators.

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: example-pdb
spec:
  selector:
    matchLabels:
      app: my-app
  minAvailable: 3
  maxUnavailable: 5 # mutually exclusive with minAvailable
```
