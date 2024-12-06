# HorizontalPodAutoscaler (hpa)

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
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 100
          periodSeconds: 15
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
        - type: Percent
          value: 100
          periodSeconds: 15
        - type: Pods
          value: 4
          periodSeconds: 15
      selectPolicy: Max
```

## Control Loop

- The control loop is executed every `15 seconds`
- The default cooldown period to scale-in is 5 minutes
