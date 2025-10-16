# Kiali

- It's required the install prometheus first!

```shell
# Manually from the istio repo
kubectl apply -f https://raw.githubusercontent.com/istio/istio/refs/heads/master/samples/addons/kiali.yaml

# With the official helm chart
helm repo add "kiali" "https://kiali.org/helm-charts"
helm install "kiali-server" "kiali/kiali-server" -n "istio-system" --set "auth.strategy=anonymous"
```

```shell
# Access the Kiali dashboard (uses port-forward)
istioctl dashboard kiali # port 20001
```

```shell
istioctl install --set "addonComponents.kiali.enabled=true"
```

## Traffic Graph

- **App graph**: Squares represent a component with label `app`
- **Versioned app graph**: App graph but subdivided into more labels, for example label `version`
- **Service graph**: Connection between services
- **Workload graph**: Workloads are analog to a deployment
