# Installation

- <https://istio.io/latest/docs/setup/getting-started/>

```shell
# Minikube setup
minikube start

# Install istioctl
brew install istioctl

# Install Istio Control Plane components on "istio-system" namespace
istioctl install --set profile=demo
istioctl install -f "istio-operator.yaml" # or install from a IstioOperator

# Configure istio to inject proxy container into pods in 'default' namespace
kubectl label namespace default istio-injection=enabled # If there are already running pods in the ns they must be restarted

# Install the official Gateway API CRD (if your cluster doesn't have it already)
kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v1.3.0" | kubectl apply -f - # installs the CRDs gateways.gateway.networking.k8s.io
```

```shell
# Deploy a distributed system
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.27/samples/bookinfo/platform/kube/bookinfo.yaml

# Create a gateway for the app
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.27/samples/bookinfo/gateway-api/bookinfo-gateway.yaml
kubectl annotate gateway bookinfo-gateway networking.istio.io/service-type=ClusterIP -n default # Change the service type to ClusterIP

# Expose the app locally
kubectl port-forward svc/bookinfo-gateway-istio 8080:80 # localhost:8080/productpage

# Send requests
for i in $(seq 1 100); do
  curl -s -o /dev/null "http://localhost:8080/productpage"
done
```

```shell
# Deploy an HTTP Server (httpbin)
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.27/samples/httpbin/httpbin.yaml

# Deploy an HTTP Client (fortio)
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.27/samples/httpbin/sample-client/fortio-deploy.yaml

# 2 concurrent connections, 20 requests
export POD=$(kubectl get pods -l app=fortio -o 'jsonpath={.items[0].metadata.name}')
kubectl exec "$POD" -c fortio -- /usr/bin/fortio load -c 2 -qps 0 -n 20 -loglevel Warning http://httpbin:8000/get
```

## Components

- Namespace **istio-system**
  - Pod `istiod`: Istio daemon
  - Pod `ingressgateway`: Control traffic in the cluster (it's a proxy)
  - Pod `egressgateway`: Control traffic out of the cluster

## Upgrading istio

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
