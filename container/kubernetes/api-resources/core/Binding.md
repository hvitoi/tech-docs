# Binding

- Binding object configures a `pod` scheduling options
- Tells to which node a pod must go

```yaml
apiVersion: v1
kind: Binding
metadata:
  name: nginx
target:
  apiVersion: v1
  kind: Node
  name: node02 # target node name
```

- Send a POST request to the binding object API to update it

```shell
curl "http://$SERVER/api/v1/namespaces/default/pods/$PODNAME/binding/" \
  --request "POST" \
  --header "Content-Type:application/json" \
  --data '{"apiVersion":"v1","kind":"Binding", ... }'
```
