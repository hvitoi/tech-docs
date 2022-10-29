# Metrics Server

- You can have 1 metrics server per kubernetes cluster
- It retrieves metrics from nodes and pods and stores it `in-memory` only
- The `kubelet` component contains a subcomponent `cAdvisor`
- `cAdvisor` retrives performance metrics from pods and expose them through the kubelet API

```sh
# Minikube
minikube addons enable "metrics-server"

# Manifest
kubectl apply -f "https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml"
```

- Metrics Server unlocks the `TOP` command

```sh
# Metrics for all pods/nodes
kubectl top pod --all-namespaces --containers=true
kubectl top node --all-namespaces --containers=true

# Metrics for a specificy pod/node
kubectl top pod "pod-name" --containers
kubectl top node "node-name" --containers
```
