# kubectl expose

- Creates a **Service Resource**
- Expose by means of a ClusterIP, NodePort, LoadBalancer, etc
- Take a `replication controller`, `service`, `deployment` or `pod` and expose it as a new Kubernetes Service

```shell
kubectl expose "deploy" "foo" \
  --type "ClusterIP" \
  --port="80"

# only generate the yaml
kubectl expose "deploy" "foo" \
  --type "NodePort" \
  --port "80" \
  --dry-run="client" \
  -o "yaml"
```
