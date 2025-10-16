# DestinationRule (dr)

- Define subsets applications. E.g., myapp-v1, myapp-v2, ...
- Define which pods should be part of which subset
- A configuration for the `Istio Load Balancing` policy

## Properties

### spec.trafficPolicy.loadBalancer

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
    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
```

### spec.trafficPolicy.connectionPool

- This is a way to implement a **circuit breaker**

```yaml
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: my-dr
spec:
  host: my-svc
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
  subsets:
    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
```

### spec.trafficPolicy.outlierDetection

```yaml
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: example-org
spec:
  host: example.org
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 1
      http:
        http1MaxPendingRequests: 1
        maxRequestsPerConnection: 1
    outlierDetection:
      consecutive5xxErrors: 1
      interval: 1s
      baseEjectionTime: 3m
      maxEjectionPercent: 100
```

### spec.subsets

- The subset elements are chosen by the matching labels (plus the host)

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

    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
      trafficPolicy: # overrides the default loadBalancer defined at spec.trafficPolicy
        loadBalancer:
          simple: ROUND_ROBIN
        connectionPool:
          tcp:
            maxConnections: 100
    - name: v3
      labels:
        version: v3
```
