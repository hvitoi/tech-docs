# Argo Workflows

- Container-native engine to orchestrate jobs in Kubernetes
- Creation and execution of complex workflows on Kubernetes

## Install

```sh
# Install
helm repo add "argo" "https://argoproj.github.io/argo-helm"
helm upgrade "argo" "argo/argo-workflows" --install \
  --namespace "argo" --create-namespace \
  --version "0.2.12"

# Access UI
kubectl -n "argo" port-forward "deployment/argo-argo-workflows-server" "2746:2746"
```
