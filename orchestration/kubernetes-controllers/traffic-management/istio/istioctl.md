# Istioctl

```shell
# Via script
curl -L https://istio.io/downloadIstio | sh -
export PATH="$PATH:$HOME/istio-1.7.1/bin"

# Via oficial releases
<https://github.com/istio/istio/releases/>

# Via Brew
brew install istioctl
```

## install

- Profiles
  - `default`: recommended for production
  - `demo`: full version for testing
  - `minimal`: only istiod
  - `remote`: multicluster mesh
  - `empty`: deploys nothing (to be used as base profile)
  - `preview`: for experimental features

```yaml
# Definition of the istio operator to be installed. It's not a CRD, just a definition
# https://raw.githubusercontent.com/istio/istio/release-1.27/samples/bookinfo/demo-profile-no-gateways.yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  profile: demo
  components:
    ingressGateways:
      - name: istio-ingressgateway
        enabled: false
    egressGateways:
      - name: istio-egressgateway
        enabled: false
```

```shell
istioctl install # uses "default" profile
istioctl install --set profile=demo # uses "demo" profile

# Specify IstioOperator directly
istioctl install -f "istio-operator.yaml"

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

## uninstall

```shell
istioctl uninstall -y --purge
kubectl delete namespace istio-system
kubectl label namespace default istio-injection-
kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v1.3.0" | kubectl delete -f - # Delete the Gateway API CRD
```

## manifest

```shell
# Transform istio manifest into a regular k8s config file
istioctl manifest generate -f "operator-file.yaml" > "k8s-config.yaml"

# Apply a istio manifest (install or reconfigure istio)
istioctl manifest install -f "operator-file.yaml" # same as istioctl install -f operator.yaml
```

## proxy-status

```shell
# Show all proxies
istioctl proxy-status
```
