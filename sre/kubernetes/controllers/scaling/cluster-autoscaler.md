# Cluster Autoscaler

> Karpenter is a newer and different approach for cluster scaling

- <https://github.com/kubernetes/autoscaler>
- It is a `controller` that runs in the cluster and automatically adjusts the size of the Cluster (number and size of nodes) based on the total resource utilization
- It uses as trigger to scale out the number of pods "pending" state

## Auto Scaling Group

- Each cloud provider has a `Scaling Group` (e.g., ASG in AWS) resource which scales VMs within a group (within the NodeGroup of the Cluster)
- The `Cluster Autoscaler` modifies the `Scaling Group` resource in order to add or remove VMs (nodes) from the cluster
- This Scaling Group has well defined `min and max boundaries` and these initially defined boundaries are always respected even if the cluster needs more nodes
- The cluster is always scaled by means of the ASG and that may take minutes.

## Permissions

- The controller needs access to the Cloud Provider Resource `Scaling Group` in order to scale the cluster it out/in

## Installation

```shell
helm install cluster-autoscaler autoscaler/cluster-autoscaler \
  --namespace kube-system \
  --set cloudProvider=<CLOUD_PROVIDER> \
  --set extraArgs.scale-down-enabled=true \
  --set rbac.create=true
```

## Annotations

```shell
kubectl annotate -n kube-system deploy/cluster-autoscaler \
  cluster-autoscaler.kubernetes.io/safe-to-evict="false"
```
