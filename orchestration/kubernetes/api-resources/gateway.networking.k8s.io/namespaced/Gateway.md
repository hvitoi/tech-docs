# Gateway (gtw)

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: bookinfo-gateway
  networking.istio.io/service-type: ClusterIP # tells istio to change the service type to ClusterIP instead of LoadBalancer (default)
spec:
  gatewayClassName: istio # requires the istio gateway controller to be installed on the cluster
  listeners:
  - name: http
    port: 80
    protocol: HTTP
    allowedRoutes:
      namespaces:
        from: Same
```
