# ScaledObject

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: cron-scaledobjecte
  namespace: default
spec:
  scaleTargetRef:
    name: my-deployment
  triggers:
    - type: cron
      metadata:
        timezone: Asia/Kolkata
        start: 30 * * * *
        end: 45 * * * *
        desiredReplicas: 10
```
