# kubectl drain

- With drain all the pods in a node are gracefully terminated in the node and moved to another node
- It's used in a preparation for maintenance when a node will go down
- The node is also marked as `unscheduled` until you remove the restriction (`uncordon`)
- The moved pod will not automatically come back to the original node
- Draining not only prevents scheduling but also evicts Pods currently running on the node to prepare it for maintenance or decommissioning

```shell
kubectl drain "node-name"
kubectl drain "node-name" --ignore-daemonsets
kubectl drain "node-name" --force # force if there are pods not managed by a Deployment, ReplicaSet, etc. The pod will then be lost forever
```
