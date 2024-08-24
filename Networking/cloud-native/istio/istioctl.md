# Istioctl

## Download

```shell
# Download istio
curl -L https://istio.io/downloadIstio | sh -

# Or visit the github
<https://github.com/istio/istio/releases/>

# Export path
export PATH="$PATH:$HOME/istio-1.7.1/bin"

# Check environment variables
env | grep istio
```

## Istio profiles

- Istio profiles
  - `default`: recommended for production
  - `demo`: full version for testing
  - `minimal`: only istiod
  - `remote`: multicluster mesh
  - `empty`: deploys nothing (to be used as base profile)
  - `preview`: for experimental features

```shell
istioctl profile list
istioctl profile dump "profile-name" > "profile-name.yaml"
istioctl profile diff "default" "demo"  # difference between default and demo

```

## Install istio

```shell
# Install Istio Operator with default profile
istioctl install
istioctl install -f "istio-operator.yaml" # specify local file containing the IstioOperator CR

# Specify repository to pull charts/profiles from
istioctl install -d "/path/to/istio-1.9.1/manifests" # local repo
istioctl install -d "https://github.com/istio/istio/releases/download/1.9.2/istio-1.9.2-linux-amd64.tar.gz" # tar repo

# Override IstioOperator value
istioctl install --set "profile=demo" # custom profile
istioctl install --set "revision=1-7" # tag to identify the istio version (this will be concatenated to the pod name)
istioctl install --set "meshConfig.enableTracing=true" # enable tracing
istioctl install --set "values.global.jwtPolicy=third-party-jwt" # authentication config preferred
```

```shell
# Configure the default namespace to inject envoy sidecar proxies
kubectl label namespace default istio-injection=enabled
```

## Install integrations (addons)

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

## Experimental commands

- Experimental command line options that might be removed in the future

```shell
# Experimental options
istioctl experimental
istioctl x

# Uninstall istio from a cluster
istioctl x uninstall --purge # Delete all revisions
istioctl x uninstall --revision "1-7" # Delete specific revision
```

## Istio Manifest

```shell
# Apply a istio manifest (install or reconfigure istio)
istioctl manifest install -f "operator-file.yaml" # same as istioctl install -f operator.yaml

# Transform istio manifest into a regular k8s config file
istioctl manifest generate -f "operator-file.yaml" > "k8s-config.yaml"
```

## Proxy

```shell
# Show all proxies
istioctl proxy-status
```

## Upgrade istio

### In-place upgrades

- Easy but risky!
- The upgrade has to be performed one by one. E.g., 1.7 to 1.8, 1.8 to 1.9
- It requires that istio was installed with istioctl

```shell
istioctl17 install # Install istio 1.7
istioctl18 upgrade # Upgrade from istio 1.7 to istio 1.8
```

- Istio cannot upgrade proxy on running pods. Therefore, after istio upgrade the pods must be restarted

```shell
kubectl rollout restart deploy
```

### Canary Upgrade

- Run a canary deployment of the new control plane
- Allow you to monitor the effect of the upgrade with a small percentage of the workloads, before migrating all of the traffic to the new version
- The tag `revision` can be used to deploy multiple independent control planes at same time
  - The revisions appears in the pod name of `istio-sidecard-injector` and `istiod`

```shell
# install istio 1.7 with corresponding revision number
istioctl17 install --set "profile=demo" --set "revision=1-7"

# check istio proxies
istioctl17 proxy-status

# install istio 1.8
istioctl18 install --set "profile=demo" --set "revision=1-8"

# check istiod versions (there will be 2 control planes runinning in parallel)
kubectl get pod -b istio-system
```

- To setup the new version of the side cards, a tag must be set for the namespace
- Now, when a pod restarts, it will have the newer istio proxy (based on the label revision)

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: default
  labels:
    istio-injection: enabled
    istio.io/rev: 1-8
```

- After validated, the old revision can be safely removed

```shell
istioctl7 x uninstall --revision "1-7"
```
