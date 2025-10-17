# Egress Gateway

- The istio gateway is a single pod that is deployed in the `istio-system` namespace
- All the `Gateway` CRDs just redirect traffic to that pod in the istio-system namespace

## Installing the Gateway

```yaml
# Make sure to have the egressGateway enabled
kind: IstioOperator
spec:
  profile: demo
  components:
    egressGateways:
      - name: istio-egressgateway
        enabled: true
```

```shell
# If you want to use the official Kubernetes Gatewas CRDs.. (otherwise you can use the istio ones)
kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v1.3.0" | kubectl apply -f -

# Check the logs of the gateway
kubectl logs -l istio=egressgateway -c istio-proxy -n istio-system -f
```

##

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
