# IstioOperator

```yaml
# IOP configuration used to install the demo profile without gateways.
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  profile: demo
  meshConfig:
    outboundTrafficPolicy:
      mode: REGISTRY_ONLY # block requests to services not in the mesh (e.g., external services)
  components:
    ingressGateways:
      - name: istio-ingressgateway
        enabled: false
    egressGateways:
      - name: istio-egressgateway
        enabled: false
```
