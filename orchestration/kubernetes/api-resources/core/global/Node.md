# Node (no)

## Properties

### metadata.labels

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

### spec.taints

- `Taints` disallow any pods to be scheduled to a node. The taint can be "bypassed" by pod `tolerations`

```yaml
apiVersion: v1
kind: Node
metadata:
  name: node01
spec:
  taints:
    # This taint is applied to master nodes. It lets only control plane components (that has the node-role.kubernetes.io/master toleration) to be scheduled to these nodes
    - key: node-role.kubernetes.io/master
      effect: NoSchedule

    # A general taint to do not allow any pod to be scheduled to this node
    - key: node.kubernetes.io/unschedulable
      effect: NoSchedule

    # Allow only GPU workloads (with the nvidia.com/gpu toleration)
    - key: nvidia.com/gpu
      value: true
      effect: NoSchedule

  unschedulable: true
```
