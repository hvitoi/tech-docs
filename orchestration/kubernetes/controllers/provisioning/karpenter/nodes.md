# Karpenter Nodes

- Nodes (VMs) created by Karpenter are `Self Managed` (managed by the Karpenter Controller).
- Differently from conventional nodes which are usually managed by a `Node Group`

## Conventional Nodes

- Karpenter eliminates the need of `Node Groups` for the main workloads
- However, you should not run Karpenter controller in the nodes managed by Karpenter itself!
- Therefore you should always have a conventional Nodes to accommodate your controllers (along with other critical components like coredns and metrics server)
  - Either by a small `Node Group` with 2 nodes in different AZs or a `Fargate Profile`
- You can use node affinity to force Karpenter controller into a specific NodeGroup

```yaml
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: karpenter.sh/nodepool
          operator: DoesNotExist
        - key: eks.amazonaws.com/nodegroup
          operator: In
          values:
          - my-node-group
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      - topologyKey: kubernetes.io/hostname
```

## Node Labels

- `topology.kubernetes.io/zone`: E.g., us-east-2a
- `node.kubernetes.io/instance-type`: E.g., g4dn.8xlarge
- `kubernetes.io/os`: E.g., linux
- `kubernetes.io/arch`: E.g., amd64
- `karpenter.sh/capacity-type`: E.g., spot
- `karpenter.k8s.aws/instance-hypervisor`: E.g., nitro
- `karpenter.k8s.aws/instance-encryption-in-transit-supported`: E.g., true
- `karpenter.k8s.aws/instance-category`: E.g., g
