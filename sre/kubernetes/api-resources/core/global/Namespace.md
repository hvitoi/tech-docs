# Namespace (ns)

- How to reach into another namespace's service from a pod
- <http://nginx.dev.svc.cluster.local/route/>
  - `cluster.local`: default domain name of the kubernetes cluster
  - `svc`: subdomain for service
  - `dev`: namespace
  - `nginx`: service name

- Deleting a namespace will delete all the objects associated with it

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: dev
spec:
  finalizers:
    - kubernetes
```

## Built-in namespaces

- Namespaces created automatically by Kubernetes

- **default**
  - Empty at the cluster creation
- **kube-node-lease**
  - Lease objects associated with each node
  - Improves performance of the nodes heartbeats
- **kube-public**
  - Accessible by all users, even unauthenticated users
- **kube-system**
  - System objects

## Namespace resources

- `ResourceQuota` restricts resource consumption on a namespace basis
- `LimitRange`: restricts resource consumption on a pod basis (so that one pod cannot monopolize the whole resource quota)

## Forcefully delete a namespace

- Resolve issues with namespaces terminating forever status

```shell
# Force delete namespace in "terminating" state
kubectl get ns "dev" -o yaml > "ns.yaml"
kubectl replace --raw "/api/v1/namespaces/dev/finalize" -f "./ns.yaml" # remove spec.finalizers[0] (kubernetes)
```
