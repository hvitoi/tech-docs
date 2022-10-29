# proxy

- Launches a proxy server locally on port `8001`
- The proxy uses the credentials and certificates from the `kubeconfig`
- The `kube-apiserver` is exposed locally with all credentials already set up

```sh
kubectl proxy
curl "localhost:8001/api"
```
