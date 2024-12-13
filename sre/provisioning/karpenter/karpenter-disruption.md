# Disruption

> A disruption refers to an event or action that causes a Pod to become unavailable or terminate. Disruptions can be voluntary or involuntary, depending on the cause

- When a disruption happens Karpenter executes a `scheduling simulation` to check if the running pods can be reallocated and `provisions replacement nodes` if needed
- Karpenter will `cordon` the nodes disrupted by adding the taint `karpenter.sh/disruption:NoSchedule` and evict pods running in it, draining the whole node

## Voluntary disruptions

- Respects the Pod Disruption Budget (PDB)
- Can be avoided with the `karpenter.sh/do-not-disrupt: true` annotation on a `Node` or any `Pod` within that node or even in the `NodePool` template itself, which applies to all nodes

### Consolidation

- Move pods around and drain underutilized nodes

### Drift

- When Karpenter CRD (NodePool or NodeClass) configuration differs from Node config
- Then the nodes need to be reconciled to the same state
- Examples:
  - New AMIs released by AWS in SSM
  - Remove existing instance type from a NodePool

### Expiration

- As defined by `nodepools.spec.template.spec.expireAfter`

## Involuntary disruptions

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

### Forced expiration

- As defined by `nodepools.spec.template.spec.terminationGracePeriod`
