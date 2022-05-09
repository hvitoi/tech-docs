# scale

- Used to scale a `ReplicaSet`, `Deployment` or a `Replication Controller`

```shell
# Scale a replicaset named 'foo' to 3
kubectl scale "rs/foo" \
  --replicas=3

# Scale a resource specified in "foo.yaml" to 3
kubectl scale \
  -f "foo.yaml" \
  --replicas=3

# If the deployment current size is 2, scale it to 3
kubectl scale "deployment/mysql" \
  --current-replicas=2 \
  --replicas=3

# Scale multiple replication controllers
kubectl scale "rc/bar" "rc/baz" "rc/foo" \
  --replicas=5
```
