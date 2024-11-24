# kubectl port-forward

- Expose a pod/svc to your localhost in a simple manner
- Good for quick tests in development mode

```shell
kubectl port-forward "pod" "host-port:container-port"
kubectl port-forward "po/my-deploy-bf89bdb5-dwxzk" "8080:80"
```
