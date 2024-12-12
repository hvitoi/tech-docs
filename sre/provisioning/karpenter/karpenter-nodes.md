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

## Node Disruption (deletion)

- **Voluntary disruptions**
  - `Expiration`: Node expiration target (hours, days) reached
  - `Drift`
  - `Consolidation`: move pods around and drain under utilized node

- **Involuntary disruptions**
  - `Spot interruption`: EC2 spot instanced reclaimed by AWS
  - `EC2 Health events`: E.g., EC2 gone
  - `Instance spot/termination events`: Someone has shut it down

- When a disruption happens Karpenter executes a `scheduling simulation` to check if the running pods can be reallocated and `provisions replacement nodes` if needed
- Karpenter will `cordon` the nodes disrupted by adding the taint `karpenter.sh/disruption:NoSchedule` to avoid new pods to be scheduled to it

### Pod Disruption Budget (PDB)

- Voluntary disruptions (by Karpenter) respects the PDB
- Involuntary disruptions may violate the PDB

### Spot Interruption

- Spot instance may be reclaimed with a 2-minutes warning
- Karpenter listens to this warning (e.g., via EventBridge in AWS) and:
  - Evicts pods in the claimed node
  - Provisions new instances (spot or demand)
  - Drains the workloads in the claimed node before the termination
