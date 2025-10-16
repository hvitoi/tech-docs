# ServiceEntry (se)

- It adds a entry to the service registry that istio will manage as if it was a service in the mesh
- It's useful for forwarding traffic to external destinations
- You can define retry, timeout, fault injection policies for external destinations

## Properties

### spec.hosts

- You can use wildcards in host

```yaml
apiVersion: networking.istio.io/v1
kind: ServiceEntry
metadata:
  name: my-se
spec:
  hosts:
    - api.dropboxapi.com
    - www.googleapis.com
    - api.facebook.com
    - example.org
  location: MESH_EXTERNAL
  ports:
    - number: 443
      name: https
      protocol: HTTPS
    - number: 80
      name: http
      protocol: TCP
  resolution: DNS
```

```yaml
# Attach a VS and DR to the ServiceEntry
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: my-vs
spec:
  hosts:
    - yahoo.com
  http:
    - route:
        - destination:
            host: yahoo.com
            port:
              number: 443
      timeout: 5s
---
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: my-dr
spec:
  host: yahoo.com
  trafficPolicy:
    connectionPool:
      tcp:
        connectTimeout: 1s
```
