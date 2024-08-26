# Litmus

```shell
helm repo add litmuschaos https://litmuschaos.github.io/litmus-helm/
helm repo list
kubectl create ns litmus
helm upgrade --install chaos litmuschaos/litmus \
  --namespace "litmus" \
  --set "portal.frontend.service.type=NodePort" \
  --set "mongodb.image.registry=ghcr.io/zcube" \
  --set "mongodb.image.repository=bitnami-compat/mongodb" \
  --set "mongodb.image.tag=6.0.5"
kubectl port-forward svc/chaos-litmus-frontend-service -n litmus 9091:9091
```
