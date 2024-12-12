# NodePool (nodepools)

- Defines what `instance types` Karpenter can create
- Based on this node pool, Karpenter will decide what is the most appropriate instance type to be created

## NodePools strategy

- **Single**
  - A single NodePool to manage compute for multiple teams and workloads
  - Use Cases
    - Mix of graviton and x86 as requirements in a single NodePool

- **Multiple**
  - Isolating compute for different purposes
  - Use Cases
    - Expensive hardware
    - Security isolation
    - Team separation
    - Different AMIs
    - Tenant isolation due to noisy neighbor

- **Weighted**
  - Define order across your NodePools so that the node scheduler will attempt to schedule with one NodePool before trying another
  - The weight for picking one nodepool over others is defined by `nodepool.spec.weight`. Higher weights are preferred
  - Use Cases
    - Prioritize `RI` and `Compute Savings Plan` ahead of other instance types. For leveraging discounts over a quota of specific EC2 instances. You want to use these discount EC2 quota first
    - Default cluster-wide configuration
    - Ratio split - Spot/OD, x86/Graviton

- Multi-NodePool strategy gotchas:
  - The pods do not need to specify the nodepool, it is automatically picked based on the requirements. If the requirements are overlapping and multiple NodePools match, the first one alphabetically is used (if not weight is defined)
  - However, it is very common that a pod does want to specify a NodePool (e.g., the Team A may only use the NodePool A). In this case it's common to define node labels in the NodePool and use then as `nodeSelector` in the pod workloads
  - The limits are isolated per NodePool

## Properties

### spec.template.metadata

- Metadata defined here will be attached to the underlying nodes
- The name of the NodePool is also added as a label in the node created. E.g., `karpenter.sh/nodepool: default`

```yaml
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: default
spec:
  template:
    metadata:
      annotations:
        application/name: my-app
      labels:
        team: my-team
    spec:
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: default
      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64", "arm64"]
        - key: kubernetes.io/os
          operator: In
          values: ["linux"]
```

### spec.template.spec.nodeCLassRef

- What NodeClass (VM configuration) to use for this node pool

```yaml
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: default
spec:
  template:
    spec:
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: default # must match the name of your NodeClass resource
      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64", "arm64"]
        - key: kubernetes.io/os
          operator: In
          values: ["linux"]
      expireAfter: 720h

  limits:
    cpu: 1000
    memory: 10000Gi
```

### spec.template.spec.requirements

- When a node is created, the same `requirement key-value pair` is added as a label in the new node

```yaml
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: default
spec:
  template:
    spec:
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: default

      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64", "arm64"]

        - key: kubernetes.io/os
          operator: In
          values: ["linux"]

        - key: node.kubernetes.io/instance-type
          operator: In
          values: ["p3.8xlarge", "p3.16xlarge"]

        - key: "topology.kubernetes.io/zone"
          operator: In
          values: ["us-west-2a", "us-west-2b"]

        # prioritizes spot
        - key: karpenter.sh/capacity-type
          operator: In
          values: ["spot", on-demand"]

        - key: karpenter.k8s.aws/instance-hypervisor
          operator: In
          values: ["nitro"]

        - key: karpenter.k8s.aws/instance-category
          operator: In
          values: ["c", "m", "r"]

        - key: karpenter.k8s.aws/instance-family
          operator: In
          values:
            - m5
            - m5d
            - c5
            - c5d
            - c4
            - r4
            - p3 # gpu

        - key: karpenter.k8s.aws/instance-generation
          operator: Gt
          values: ["2"]

        - key: karpenter.k8s.aws/instance-cpu
          operator: In
          values: ["4", "8", "16", "32"]

        - key: karpenter.k8s.aws/instance-size
          operator: NotIn
          values: ["nano","micro","small"]

      expireAfter: 720h # 30 * 24h = 720h

  limits:
    cpu: 1000
    memory: 10000Gi

  disruption:
    consolidationPolicy: WhenEmptyOrUnderutilized
    consolidateAfter: 1m
```

### spec.template.spec.taints

- Taints defined here will be attached to the underlying nodes

```yaml
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: default
spec:
  template:
    spec:
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: default
      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64", "arm64"]
        - key: kubernetes.io/os
          operator: In
          values: ["linux"]
      taints:
        # only gpu workloads (with the nvidia.com/gpu toleration) will run on the node
        - key: nvidia.com/gpu
          value: true
          effect: NoSchedule
```

### spec.limits

- Hard limits for all instances in the node pool

```yaml
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: default
spec:
  template:
    spec:
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: default
      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64", "arm64"]
        - key: kubernetes.io/os
          operator: In
          values: ["linux"]
  limits:
    cpu: 1000
    memory: 10000Gi
```

### spec.weight

- Hard limits for all instances in the node pool

```yaml
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: default
spec:
  template:
    spec:

      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: default

      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64", "arm64"]
        - key: kubernetes.io/os
          operator: In
          values: ["linux"]

  weight: 60
```

### spec.disruption

- Tells Karpenter when/how to disrupt nodes
- Actions
  - Remove empty nodes
  - Remove nodes by moving pods to another underutilized node
  - Replace nodes with cheaper variants

```yaml
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: default
spec:
  template:
    spec:
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: default
      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64", "arm64"]
        - key: kubernetes.io/os
          operator: In
          values: ["linux"]
  disruption:
    consolidationPolicy: WhenEmptyOrUnderutilized
    # consolidationPolicy: WhenEmpty
    # consolidationPolicy: WhenUnderutilized
    consolidateAfter: 1m # how much to wait to scale nodes down due to low utilization
    expiresAfter: Never
```
