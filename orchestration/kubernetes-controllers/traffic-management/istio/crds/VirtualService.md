# VirtualService (vs)

- Configures how requests are routed to a service
- Consists of a set of routing rules, that are `evaluated in sequential order from top to bottom`
- Without virtual services, Envoy distributes traffic using least requests load balancing between all service instances
- Virtual services act in the istio-daemon. It updates all the DNS from the proxies inside all the pods dynamically

## Matching by header

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

## Matching by URI

```yaml
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

## Weighted destination

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
          weight: 75
        - destination:
            host: reviews
            subset: v2
          weight: 25
```

## From Gateway

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
