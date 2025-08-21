# Metrics Server

- You can have 1 metrics server per Kubernetes cluster
- It retrieves metrics from nodes and pods and stores it `in-memory` only
- Metrics Server is **meant only for autoscaling purposes** (`Horizontal Pod Autoscaler` and `Vertical Pod Autoscaler`). For example, don't use it to forward metrics to monitoring solutions, or as a source of monitoring solution metrics. In such cases please collect metrics from Kubelet `/metrics/resource` endpoint directly

```shell
# Minikube
minikube addons enable "metrics-server"

# Manifest
kubectl apply -f "https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml"
```

## Kubelet cAdisor

- The `kubelet` contains a subcomponent `cAdvisor`
- `cAdvisor` retrives performance metrics from pods and expose them through the kubelet API endpoint **/metrics/resource**
- Metrics Server collects resource metrics from these kubelets and exposes them in `Kubernetes apiserver` through Metrics API

## kubectl top

- Metrics Server unlocks the `TOP` command

```shell
# Metrics for all pods/nodes
kubectl top pod --all-namespaces --containers=true
kubectl top node --all-namespaces --containers=true

# Metrics for a specificy pod/node
kubectl top pod "pod-name" --containers
kubectl top node "node-name" --containers
```
