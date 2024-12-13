# Karpenter Nodes

- Nodes (VMs) created by Karpenter are `Self Managed` (managed by the Karpenter Controller).
- Differently from conventional nodes which are usually managed by a `Node Group`
- Karpenter eliminates the need of `Node Groups`

## Node Labels

- `topology.kubernetes.io/zone`: E.g., us-east-2a
- `node.kubernetes.io/instance-type`: E.g., g4dn.8xlarge
- `kubernetes.io/os`: E.g., linux
- `kubernetes.io/arch`: E.g., amd64
- `karpenter.sh/capacity-type`: E.g., spot
- `karpenter.k8s.aws/instance-hypervisor`: E.g., nitro
- `karpenter.k8s.aws/instance-encryption-in-transit-supported`: E.g., true
- `karpenter.k8s.aws/instance-category`: E.g., g
