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

## Disruption

> A disruption refers to an event or action that causes a Pod to become unavailable or terminate. Disruptions can be voluntary or involuntary, depending on the cause

- **Voluntary disruptions**
  - `Expiration`
  - `Drift`
  - `Consolidation`

- **Involuntary disruptions**
  - `Spot Interruption`
  - `EC2 Health events`
  - `Instance spot/termination events`

- When a disruption happens Karpenter executes a `scheduling simulation` to check if the running pods can be reallocated and `provisions replacement nodes` if needed
- Karpenter will `cordon` the nodes disrupted by adding the taint `karpenter.sh/disruption:NoSchedule` and evict pods running in it, draining the whole node
- Voluntary disruptions respect the Pod Disruption Budget (PDB)

### Expiration

- Node expiration target (hours, days) reached

### Drift

- When Karpenter CRD (NodePool or NodeClass) configuration differs from Node config
- Then the nodes need to be reconciled to the same state
- Examples:
  - New AMIs released by AWS in SSM
  - Remove existing instance type from a NodePool

### Consolidation

- Move pods around and drain underutilized nodes

### Spot Interruption

- Spot instance may be reclaimed with a 2-minutes warning
- Karpenter listens to this warning (e.g., via EventBridge AWS::Events::Rule to a target queue AWS::SQS::Queue) and:
  - Evicts pods in the claimed node
  - Provisions new instances (spot or demand)
  - Drains the workloads in the claimed node before the termination

### EC2 Health events

- E.g., EC2 gone

### Instance spot/termination events

- Someone has shut the instance down
