# CloudNativePG (CNPG)

- Kubernetes operator for running PostgreSQL clusters
- Manages primary/replica topology, failover, backups, and connection routing via auto-created Services
-

## Installation

```shell
# Install the operator
kubectl apply --server-side -f "https://raw.githubusercontent.com/cloudnative-pg/cloudnative-pg/release-1.29/releases/cnpg-1.29.1.yaml"

# Verify
kubectl rollout status deployment -n cnpg-system cnpg-controller-manager
```

## Create a cluster

- No Deployment or StatefulSet is created, the CR manages the pods directly, rather than delegating to a built-in workload controller

```shell
# Create a cluster
kubectl apply -f Cluster.yaml

# Watch pods
kubectl get pods -l cnpg.io/cluster=mycluster -w
```

## Connect to cluster

The operator auto-creates Services and a Secret with credentials:

- `mycluster-rw` → read/write (primary)
- `mycluster-ro` → read-only (replicas)
- `mycluster-r`  → any instance

```shell
# password for the default 'app' user / 'app' database
kubectl get secret mycluster-app -o jsonpath='{.data.password}' | base64 -d

# port-forward and connect
kubectl port-forward svc/mycluster-rw 5432:5432
psql -h localhost -U app -d app
```

```shell
# cnpg kubectl plugin
kubectl krew install cnpg
kubectl cnpg status pg-cluster
```
