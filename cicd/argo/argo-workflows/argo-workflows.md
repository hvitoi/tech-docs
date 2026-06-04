# Argo Workflows

- Engine to orchestrate parallel jobs on Kubernetes
- Each step in a workflow run as a pod
- Used for CI pipelines, batch processing, ML training, ETL, data processing
- Supports `DAGs`, `fan-out,fan-in`, `conditionals`, `retries`, `artifacts` (passing files between steps via S3, GCS, etc)
- It's the "CI" part in a CI/CD platform: build, test, package, scans

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
