# Istio CRDs

- There are two main CRDs in Istio
  - `VirtualServices`
  - `DestinationRules`

```shell
# Virtual services
kubectl get virtualservice
kubectl get vs

# Destination rules
kubectl get destinationrules
kubectl get dr
```

- VS ad DR can be deleted on `Delete all traffic routing`
