# kubectl edit

- Opens a prompt to edit a yaml manifest

```shell
kubectl edit "object-type" "object-name"
kubectl edit "svc" "mysvc"
kubectl edit "svc/mysvc"

KUBE_EDITOR="vim" kubectl edit "svc/mysvc"
```

## --output-version

```shell
# Edit the service 'mysvc' in JSON using the v1 API format:
kubectl edit "svc/mysvc" \
  --output-version="v1" \
  -o "json"
```

## --record

- Record the change as a new revision for rollback purposes in a Deployment

```shell
kubectl edit "deployment/my-depl" --record=true
```
