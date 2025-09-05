# kubectl taint

- Offer restrictions to what pods can be scheduled on which node
- The `master` nodes are automatically tainted! That prevents any pods to be scheduled there

## Taint & Toleration

- `Taint`: repeal to a specific pod. It's applied to the `node`
- `Toleration`: tolerance that a `pod` has to a specific node taint. If not specified, pods have no tolerations. Toleration does not guarantee that a pod will be scheduled to the tolerated pod

## Taint Effects

- 3 Taint Effects
  - `NoSchedule`: pods cannot be scheduled on the node
  - `PreferNoSchedule`: pods are avoided scheduling on this node
  - `NoExecute`: new pods will not be scheduled on this node, existing pods will be evicted on this node (it will be killed soon and recreated in another node)

```shell
# Apply taints to a node
kubectl taint "no" "node-name" \
  "app=blue:NoSchedule"

kubectl taint "no" "node-name" \
  "app=value:PreferNoSchedule"

kubectl taint "no" "node-name" \
  "app=blue:NoExecute"

# Remove taint
kubectl taint "no" "node-name" \
  "node-role.kubernetes.io/master:NoSchedule"-
```
