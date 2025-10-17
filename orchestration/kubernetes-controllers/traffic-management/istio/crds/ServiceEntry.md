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
  ports:
    - number: 80
      name: http
      protocol: HTTP
    - number: 443
      name: https
      protocol: HTTPS
  resolution: DNS
  location: MESH_EXTERNAL
```

- You can then attach VS and DR to the service

### spec.ports

- Specify which the ports of incoming requests to the host that should be managed by istio

```yaml
apiVersion: networking.istio.io/v1
kind: ServiceEntry
metadata:
  name: my-se
spec:
  hosts:
    - example.org
  ports:
    # tells istio to do not pass through http and https requests
    - number: 80
      name: http-port
      protocol: HTTP
    - number: 443
      name: https-port
      protocol: HTTPS
  resolution: DNS
  location: MESH_EXTERNAL
```

### spec.resolution

- `NONE`: Insecure!
  - A malicious client could pretend that it's accessing httpbin.org by setting it in the HOST header, while really connecting to a different IP (that is not associated with httpbin.org). The istio sidecar trusts the host header
- `DNS`: Istio ignores the host header and it performs the DNS resolution itself to get the correct IP address

```yaml
apiVersion: networking.istio.io/v1
kind: ServiceEntry
metadata:
  name: my-se
spec:
  hosts:
    - example.org
  ports:
    - number: 80
      name: http-port
      protocol: HTTP
    - number: 443
      name: https-port
      protocol: HTTPS
  resolution: DNS
  location: MESH_EXTERNAL
```
