# HorizontalPodAutoscaler

- Automatically scales a resource based on `CPU` utilization
  - Deployment
  - Replication Controller
  - StatefulSet
- `HPA` needs the `metrics server` installed in order to watch the metrics

```yaml
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: currency-exchange
spec:
  minReplicas: 1
  maxReplicas: 3
  targetCPUUtilizationPercentage: 70
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: currency-exchange
```

- Default cooldown period to scale in is 5 minutes
