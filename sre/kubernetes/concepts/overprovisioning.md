# Cluster Overprovisioner

- <https://kubernetes.io/docs/tasks/administer-cluster/node-overprovisioning/>
- It's possible to create `pre-warmed` nodes with `pause/dummy` pods. Each dummy pod will accommodate itself in a node alone
- This purposely over-provisions the cluster in order to give headroom for a sudden spike of load
- It's also possible to set the number of dummy pods proportional to the total number of nodes in the cluster
