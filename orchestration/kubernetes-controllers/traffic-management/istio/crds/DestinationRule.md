# DestinationRule (dr)

- Define subsets applications. E.g., myapp-v1, myapp-v2, ...
- Define which pods should be part of which subset
- A configuration for the `Istio Load Balancing` policy

## Load balancer

- <https://istio.io/latest/docs/concepts/traffic-management/#load-balancing-options>

- `Random`: Requests are forwarded at random to instances in the pool.
- `Weighted`: Requests are forwarded to instances in the pool according to a specific percentage.
- `Round robin`: Requests are forwarded to each instance in sequence.
- `Consistent hash`: Provides soft session affinity based on HTTP headers, cookies or other properties.
- `Ring hash`: Implements consistent hashing to upstream hosts using the Ketama algorithm.
- `Maglev`: Implements consistent hashing to upstream hosts as described in the Maglev paper.

```yaml
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: my-dr
spec:
  host: my-svc
  trafficPolicy:
    loadBalancer: # by default uses the "least requests" load balancing policy
      simple: RANDOM
  subsets:
    # The subset elements are picked by the matching labels (plus the host)
    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
      trafficPolicy: # overrides the default loadBalancer defined at spec.trafficPolicy
        loadBalancer:
          simple: ROUND_ROBIN
    - name: v3
      labels:
        version: v3
```
