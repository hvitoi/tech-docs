# Prometheus

```shell
# Manually from the istio repo
kubectl apply -f  https://raw.githubusercontent.com/istio/istio/refs/heads/master/samples/addons/prometheus.yaml

# With the official helm chart
helm repo add "prometheus-community" "https://prometheus-community.github.io/helm-charts"
helm install "prometheus" "prometheus-community/prometheus" -n "istio-system"
```

```shell
istioctl install --set "addonComponents.grafana.enabled=true"
```

```shell
istioctl dashboard "prometheus"
```
