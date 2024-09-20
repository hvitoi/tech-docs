# Rollout

- Manage the rollout of a `daemonset`, `deployment` or `statefulset` resource.

## Status

```shell
# Check the rollout status of a resource
kubectl rollout status deployment "foo"
kubectl rollout status daemonset "foo"
kubectl rollout status statefulset "foo"
```

## History

```shell
# Show revisions history (records last 10 by default)
kubectl rollout history deployment "foo"

# Show a specific revision
kubectl rollout history deployment "foo" --revision=1
```

## Undo

```shell
# Rollback to previous revision
kubectl rollout undo deployment "foo"

# Rollback to specific revision
kubectl rollout undo deployment "foo" --to-revision "3"
```

## Restart

```shell
# Restart current revision
kubectl rollout restart deployment # from all deployments
kubectl rollout restart deployment "foo" # from specific deployment
kubectl rollout restart -f "manifest.yaml" # from manifest
```

## Pause

- Pause the deployment controller so that no pods are rolled out
- It's useful when you want to perform multiple imperative commands and resume only after all of them have been executed

```shell
kubectl rollout pause deployment "foo"
```

## Resume

- Resume deployment controlling

```shell
kubectl rollout resume deployment "foo"
```
