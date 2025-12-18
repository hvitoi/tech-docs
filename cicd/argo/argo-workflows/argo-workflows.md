# Argo Workflows

- Container-native engine to orchestrate jobs in Kubernetes
- Creation and execution of complex workflows on Kubernetes

## Install Operator

```shell
# With Helm
helm repo add "argo" "https://argoproj.github.io/argo-helm"
helm upgrade "argo" "argo/argo-workflows" --install \
  --namespace "argo" --create-namespace \
  --version "0.2.12"

# With Manifests
kubectl create namespace argo
kubectl apply -n argo -f "https://github.com/argoproj/argo-workflows/releases/download/vX.Y.Z/quick-start-minimal.yaml"
```

## Install CLI

```shell
# Via brew
brew install argo

# Via binary
# https://github.com/argoproj/argo-workflows/releases/
```

## Access UI

```shell
kubectl -n argo port-forward service/argo-server 2746:2746
```
