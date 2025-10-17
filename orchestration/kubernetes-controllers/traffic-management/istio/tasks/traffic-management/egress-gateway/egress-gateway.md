# Egress Gateway

```shell
istioctl install --set values.pilot.env.PILOT_ENABLE_ALPHA_GATEWAY_API=true --set profile=minimal -y
```

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
