# port-forward

- Expose a pod/svc to your localhost in a simple manner
- Good for quick tests in development mode

```sh
kubectl port-forward "pod" "host-port:pod-port"
kubectl port-forward "nats-depl-69c8746f74-hds9f" "4222:4222"
```
