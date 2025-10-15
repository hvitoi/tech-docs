# Installation

- <https://istio.io/latest/docs/setup/getting-started/>

```shell
# Minikube setup
minikube start --memory 4g

# Install istioctl
brew install istioctl

# Install Istio Control Plane components on "istio-system" namespace
istioctl install --set profile=demo

# Configure istio to inject proxy container into pods in 'default' namespace
kubectl label namespace default istio-injection=enabled # If there are already running pods in the ns they must be restarted

# Install the official Gateway API CRD (if your cluster doesn't have it already)
kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || { kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v1.3.0" | kubectl apply -f -; }

# Deploy a sample application
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.27/samples/bookinfo/platform/kube/bookinfo.yaml

# Create a gateway for the app
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.27/samples/bookinfo/gateway-api/bookinfo-gateway.yaml
kubectl annotate gateway bookinfo-gateway networking.istio.io/service-type=ClusterIP -n default # Change the service type to ClusterIP

# Access the app
kubectl port-forward svc/bookinfo-gateway-istio 8080:80
```

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
