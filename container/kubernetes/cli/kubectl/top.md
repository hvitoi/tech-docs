# top

- The `top` command allows you to see the resource consumption for `nodes` or `pods`.
- This command requires `Metrics Server` to be correctly configured and working on the server.

```shell
# Metrics for all pods/nodes
kubectl top pod --all-namespaces --containers=true
kubectl top node --all-namespaces --containers=true

# Metrics for a specificy pod/node
kubectl top pod "pod-name" --containers
kubectl top node "node-name" --containers
```
