# expose

- Creates a **Service Resource**
- Expose by means of a ClusterIP, NodePort, LoadBalancer, etc
- Take a `replication controller`, `service`, `deployment` or `pod` and expose it as a new Kubernetes Service

```sh
kubectl expose "deployment" "ingress-nginx-controller" \
  -namespace "kube-system" \
  --type="ClusterIP" \
  --target-port="80"
```

```sh
kubectl expose "pod" "my-pod" \
  --name "my-svc"
  --port "6379" \
  --dry-run="client" \
  -o "yaml" \
  > "service.yaml"
```
