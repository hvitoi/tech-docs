# ingress-nginx

- <<https://kubernetes.github.io/ingress-nginx>>
- The Ingress Controller Pods are exposed as a single `LoadBalancer` (or NodePort)
- The Ingress Controller Pods have a single `Public IP` (must be created beforehand) - `az network public-ip create ...`
- All the external traffic now passed through one of the ingress controller replicas

```shell
# create public IP for the ingress controller pods
az network public-ip create \
  --resource-group "MC_aks-rg_aks-cluster_southcentralus" \ # must be the "nodeResourceGroup"
  --name "aks-ingress-ip" \
  --sku "Standard" \
  --allocation-method "static" \ # static IP!
  --query "publicIp.ipAddress" \
  -o "tsv"
```

```shell
helm install "ingress-controller" "ingress-nginx/ingress-nginx" \
  --namespace "ingress" --create-namespace \
  --version "3.30.0" \
  --set controller.replicaCount=3 \
  --set controller.service.externalTrafficPolicy=Local \
  --set controller.service.loadBalancerIP=000.000.000.000 \ # public IP created beforehand
  --set controller.nodeSelector."beta\.kubernetes\.io/os"=linux \ # controller must run on a linux worker
  --set defaultBackend.nodeSelector."beta\.kubernetes\.io/os"=linux # defaultbackend must run on a linux worker

# ... for nodeport (not recommended)
  --set "controller.service.type=NodePort" \
  --set "controller.service.nodePorts.https=31000" \

# .. for ssl
  --set "controller.extraArgs.enable-ssl-passthrough=""" \
  --set "controller.extraArgs.default-ssl-certificate=ingress/ingress-tls"
```
