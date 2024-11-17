# kubectl cp

```shell
# Copy from local to remote pod
kubectl cp "/tmp/foo_dir" "some-pod":"/tmp/bar_dir"

# Copy from a remote pod to local
kubectl cp "some-namespace"/"some-pod":"/tmp/foo" "/tmp/bar"
```
