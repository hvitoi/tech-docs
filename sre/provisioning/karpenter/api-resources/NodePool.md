# NodePool (nodepools)

- Defines what `instance types` Karpenter can create
- Based on this node pool, Karpenter will decide what is the most appropriate instance type to be created

## Properties

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
          values: ["m5","m5d","c5","c5d","c4","r4"]

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
