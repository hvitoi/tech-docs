# Install integrations (addons)

- Software that istio can integrate to provide additional functionality
  - `cert-manager`
  - `jaeger`
  - `prometheus`
  - `grafana`
  - `kiali`
  - `zipkin`

- Addons can be applied from <istio-1.9.1/samples/addons> for testing
  - E.g., `kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.9/samples/addons/prometheus.yaml`

```shell
# Prometheus
helm repo add "prometheus-community" "https://prometheus-community.github.io/helm-charts"
helm install "prometheus" "prometheus-community/prometheus" -n "istio-system"
helm delete "prometheus" -n "istio-system"
istioctl dashboard "prometheus"

# Kiali (default port: 20001)
helm repo add "kiali" "https://kiali.org/helm-charts"
helm install "kiali-server" "kiali/kiali-server" -n "istio-system" --set "auth.strategy=anonymous"
istioctl dashboard "kiali" # port-forward the kiali UI

istioctl install --set "addonComponents.kiali.enabled=true" # Kiali
istioctl install --set "addonComponents.grafana.enabled=true" # Grafana
```
