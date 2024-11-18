# kubectl Rollout

- Manage the rollout of a `daemonset`, `deployment` or `statefulset` resource.

## status

```shell
# Check the rollout status of a resource
kubectl rollout status deployment "foo"
kubectl rollout status daemonset "foo"
kubectl rollout status statefulset "foo"
```

## history

```shell
# Show revisions history (records last 10 by default)
kubectl rollout history deployment "foo"

# Show a specific revision
kubectl rollout history deployment "foo" --revision=1
```

## restart

- Restarts the current revision

```shell
kubectl rollout restart deployment # from all deployments
kubectl rollout restart deployment "foo" # from specific deployment
kubectl rollout restart -f "manifest.yaml" # from manifest
```

## pause

- Pause the deployment controller so that no pods are rolled out
- It's useful when you want to perform multiple imperative commands and resume only after all of them have been executed
- While a deployment is paused, the changes do not appear in the `rollout history`. The revision is created only when it is unpaused and as a single revision (even if multiple edits have been made)

```shell
kubectl rollout pause deployment "foo"
```

## resume

- Resume deployment controlling

```shell
kubectl rollout resume deployment "foo"
```

## undo

- When a rollback is made to a specific revision, this revision is bubbled up to the last revision
  - Example: Given the revisions `Rev1, Rev2, Rev3` when rolling out to Rev2 it goes to the last revision as a new one `Rev1, Rev3, Rev4`

```shell
# Rollback to the previous revision
kubectl rollout undo deployment "foo"

# Rollback to specific revision
kubectl rollout undo deployment "foo" --to-revision "3"
```
