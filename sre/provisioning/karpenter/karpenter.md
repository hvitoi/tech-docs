# Karpenter

- A cluster scaler
- Periodically checks for `pending unschedulable pods` and when that's the case create new nodes
- Karpenter provisions the `appropriate VM` based on the podspec of the pending pod
- Other benefits
  - Cost optimization
  - Supports diverse workloads including ML and gen AI
  - Helps upgrade and patching
  - Kubernetes native

> Karpenter was created by AWS but has been open sourced

## Karpenter Nodes

- Nodes (VMs) created by Karpenter are `Self Managed` (managed by the Karpenter Controller).
- Differently from conventional nodes which are usually managed by a `Node Group`
- Karpenter eliminates the need of `Node Groups`

### Node Labels

- `topology.kubernetes.io/zone`: E.g., us-east-2a
- `node.kubernetes.io/instance-type`: E.g., g4dn.8xlarge
- `kubernetes.io/os`: E.g., linux
- `kubernetes.io/arch`: E.g., amd64
- `karpenter.sh/capacity-type`: E.g., spot
- `karpenter.k8s.aws/instance-hypervisor`: E.g., nitro
- `karpenter.k8s.aws/instance-encryption-in-transit-supported`: E.g., true
- `karpenter.k8s.aws/instance-category`: E.g., g

## Karpenter vs. Cluster Autoscaler

- Karpenter bypasses the flow of creating new nodes by means of the ASG of a Node Group that Cluster Autoscaler uses. Instead Karpenter creates new VMs directly
- Also, Node Groups and their ASGs contain identical VMs of the same instance type. This may be not desirable as each pending workload may require different types of hardware (e.g., GPU processes). Karpenter provisions individual VMs of the appropriate type.
- With Karpenter, `Node Groups are not even necessary`. The VMs are attached directly to the cluster and Karpenter manages it

## Spot Interruption Handler

- Spot instance may be reclaimed with a 2-minutes warning
- Karpenter listens to this warning (e.g., via EventBridge in AWS) and:
  - Evicts pods in the claimed node
  - Provisions new instances (spot or demand)
  - Drains the workloads in the claimed node before the termination
