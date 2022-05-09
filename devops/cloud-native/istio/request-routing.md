# Request routing

## Request matching

- Request matching
  - By header
  - By URI
  - By scheme
  - By method
  - By authority

## Virtual service

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: fleetman-driver-monitoring
spec:
  hosts:
    - 2oujlno5e4.execute-api.us-east-1.amazonaws.com
  http:
    - match:
        - port: 80
      route:
        - destination:
            host: 2oujlno5e4.execute-api.us-east-1.amazonaws.com
            port:
              number: 443
```

## Destination rule

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: fleetman-driver-monitoring
spec:
  host: 2oujlno5e4.execute-api.us-east-1.amazonaws.com
  trafficPolicy:
    loadBalancer:
      simple: ROUND_ROBIN
    portLevelSettings:
      - port:
          number: 443
        tls:
          mode: SIMPLE
```
