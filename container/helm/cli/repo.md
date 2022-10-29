# repo

```sh
# List repos
helm repo list

# Add google official repo
helm repo add "repo-name" "repo-url"

# Update chart list
helm repo update
```

```sh
helm repo add "stable" "https://kubernetes-charts.storage.googleapis.com/"
helm repo add "strimzi" "https://strimzi.io/charts/"
helm repo add "ingress-nginx" "https://kubernetes.github.io/ingress-nginx"
helm repo add "prometheus-community" "https://prometheus-community.github.io/helm-charts"
helm repo add "akhq" "https://akhq.io/"
helm repo add "kiali" "https://kiali.org/helm-charts"
helm repo add "argo" "https://argoproj.github.io/argo-helm"
```
