# kubectl edit

- Opens a prompt to edit a yaml manifest

```shell
# Edit an object
kubectl edit "object-type" "object-name"
kubectl edit "svc" "my-service"
kubectl edit "svc/mysvc"
kubectl edit "deployment/my-depl" --record=true # record for rollback purposes

# Use an alternative editor
KUBE_EDITOR="vim" kubectl edit "svc/mysvc"

# Edit the service 'mysvc' in JSON using the v1 API format:
kubectl edit "svc/mysvc" \
  --output-version="v1" \
  -o "json"
```
