# Namespace

- How to reach into another namespace's service from a pod
- <http://nginx.dev.svc.cluster.local/route/>

  - `cluster.local`: default domain name of the kubernetes cluster
  - `svc`: subdomain for service
  - `dev`: namespace
  - `nginx`: service name

- Namespaces created automatically by kubernetes
  - default
  - kube-system
  - kube-public

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: dev
spec:
  finalizers:
    - kubernetes
```

## Resources

- `ResourceQuota` restricts resource consumption on a namespace basis
- `LimitRange`: restricts resource consumption on a pod basis (so that one pod cannot monopolize the whole resource quota)

## Terminating forever status

```shell
# Force delete namespace in "terminating" state
kubectl get ns "dev" -o yaml > "ns.yaml"
kubectl replace --raw "/api/v1/namespaces/dev/finalize" -f "./ns.yaml" # remove spec.finalizers[0] (kubernetes)
```
