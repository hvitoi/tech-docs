# External Services

- All requests to unknown services (services that are not configured inside the mesh) are passed through by Istio (e.g., external services)
- Alternatively you can configure `Service Entries` add those external services to the mesh

## Blocking Unknown Services

- You can modify the option `meshConfig.outboundTrafficPolicy.mode` to:
  - `REGISTRY_ONLY`: block connections to all unknown services
  - `ALLOW_ANY`: bypasses envoy when connecting to unknown services

## Adding services to the mesh

- External externas can be added to the mesh using `ServiceEntry` configurations

## HTTPS services

- `HTTPS` requests are always passed through!

## Testing

```shell
# Deploy an HTTP Client (curl)
kubectl apply -f curl-client.yaml

# Apply the mesh config to the external service
kubectl apply -f mesh-config.yaml

# Monitor the proxy logs
kubectl logs test-curl -c istio-proxy -f
# It explicitly shows "PassthroughCluster" if it's not managed by istio. But sometimes (e.g., for https connections) it won't show passthrough although it's not managed by istio

# Send requests
kubectl exec test-curl -- curl -sSI https://postman-echo.com/delay/1
# it will show "server: cloudflare" if it's passed through, and "server: envoy" if it's routed through envoy
```
