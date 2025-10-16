# VirtualService (vs)

- Configures how requests are routed to a service
- Consists of a set of routing rules, that are `evaluated in sequential order from top to bottom`
- Without virtual services, Envoy distributes traffic using least requests load balancing between all service instances
- Virtual services act in the istio-daemon. It updates all the DNS from the proxies inside all the pods dynamically

## Properties

### spec.hosts

```yaml
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
    - reviews # to what hosts this rule applies to. Wildcards can be used
  http:
    - match:
        - headers:
            end-user:
              exact: jason
      route:
        - destination:
            host: reviews
            subset: v2
    - route:
        - destination:
            host: reviews
            subset: v3
```

### spec.gateways

- Get traffic from gateway

```shell
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: virtual-svc
spec:
  hosts:
    - ext-host.example.com
  gateways:
    - ext-host-gwy
```

### spec.http.[].match.[]

```yaml
# Matching by header
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
    - reviews # to what hosts this rule applies to. Wildcards can be used
  http:
    - match:
        - headers:
            end-user:
              exact: jason # requests with this header go the v2 app
      route:
        - destination:
            host: reviews # where to actually route the request
            subset: v2 # a subset is created with a DestinationRule
    - route: # default rule (no matching condition - "catch all")
        - destination:
            host: reviews
            subset: v3
```

```yaml
# Matching by URI
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: bookinfo
spec:
  hosts:
    - bookinfo.com
  http:
    - match:
        - uri:
            prefix: /reviews
      route:
        - destination:
            host: reviews
    - match:
        - uri:
            prefix: /ratings
      route:
        - destination:
            host: ratings
```

### spec.http.[].route.[]

```yaml
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
    - reviews
  http:
    - route: # no match condition is used, just the weighted destinations
        - destination:
            host: reviews
            subset: v1
          weight: 75 # Weighted destination
        - destination:
            host: reviews
            subset: v2
          weight: 25
```

### spec.http.[].timeout

- This timeout implemented here means that http calls to this host will timeout after X seconds

```yaml
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: ratings
spec:
  hosts:
    - ratings
  http:
    - route:
        - destination:
            host: ratings
            subset: v1
      timeout: 10s
```

### spec.http.[].retries

```yaml
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: ratings
spec:
  hosts:
    - ratings
  http:
    - route:
        - destination:
            host: ratings
            subset: v1
      retries:
        attempts: 3
        perTryTimeout: 2s
```

### spec.http.[].fault

```yaml
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: my-vs
spec:
  hosts:
    - ratings
  http:
    - fault:
        delay: # inject a delay fault
          percentage:
            value: 100
          fixedDelay: 2s
      route:
        - destination:
            host: ratings
            subset: v1
```
