# LimitRange

- Enforce min or max `resource usage` or `storage usage` per container
- Enforce ratio between request and limit
- Enforce default `resource limits` and `resource requests`

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: my-limit-range
  namespace: dev # to which ns these rules apply
spec:
  limits:
    - type: Container
      defaultRequest: # request
        memory: 256Mi # defaults to same as the limit
        cpu: 0.5 # defaults to same as the limit
      default: # limit
        memory: 512Mi # defaults the namespace default
        cpu: 1 # defaults to 1000m
```
