# Istio Config

```shell
# Get all
kubectl get configmap istio -n istio-system -o yaml

# Modify config
istioctl install --set meshConfig.outboundTrafficPolicy.mode=ALLOW_ANY
```
