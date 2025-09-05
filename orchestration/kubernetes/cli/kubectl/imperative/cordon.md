# kubectl cordon

- Mark a node as `unschedulable`
- Cordon makes the node `no.spec.unschedulable = true` and adds a `taint` to a node to avoid it being considered by kube-schedule
- It `does not evict` pods already running in the not. It just prevents new ones from being scheduled there
- `cordon` (kubectl cordon) is often used as the first step before `draining` a node (kubectl drain)

```shell
kubectl cordon "node-name"
```

```yaml
apiVersion: v1
kind: Node
metadata:
  name: ip-192-168-124-41.ec2.internal
spec:
  taints:
    - key: node.kubernetes.io/unschedulable
      effect: NoSchedule
      timeAdded: "2024-12-12T00:40:34Z"
  unschedulable: true
```
