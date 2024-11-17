# Node (no)

## Labels

- Labels are useful for node selecting

```yaml
apiVersion: v1
kind: Node
metadata:
  name: node01
  labels:
    beta.kubernetes.io/arch: amd64
    beta.kubernetes.io/os: linux
    kubernetes.io/arch: amd64
    kubernetes.io/hostname: mymachine.openstack.internal
    kubernetes.io/os: linux
    node-role.kubernetes.io/master: ""
    size: large
spec:
  podCIDR: 10.200.0.0/24
  podCIDRs:
    - 10.200.0.0/24
```

## Taints

- `master` nodes are automatically tainted! That prevents any pods to be scheduled there

```yaml
apiVersion: v1
kind: Node
metadata:
  name: node01
spec:
  podCIDR: 10.200.0.0/24
  podCIDRs:
    - 10.200.0.0/24
  taints:
    - key: node-role.kubernetes.io/master
      effect: NoSchedule
    - key: node.kubernetes.io/unschedulable
      effect: NoSchedule
  unschedulable: true
```
