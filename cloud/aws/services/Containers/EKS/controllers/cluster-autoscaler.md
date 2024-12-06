# Cluster Autoscaler

> This is a cloud-agnostic controller, for more info check the Kubernetes tech-docs directly

- What this controller does is to adjust the resource `AWS::AutoScaling::AutoScalingGroup` of the NodeGroups based on the total usage of the cluster
- The `ASG` already have min and max nodes defined at the `NodeGroup` creation. Autoscaler will obey this boundaries. Example: if the max number of nodes is 4 but there are still pending pods, autoscaler won't launch new nodes.

## Permissions

- The controller needs access to the `AutoScalingGroup` AWS Resource in order scale out/in the EC2 Instances
- Pass the flag `--asg-access` when creating the NodeGroup via `eksctl` so that the workloads running in the worker nodes have access to ASG
