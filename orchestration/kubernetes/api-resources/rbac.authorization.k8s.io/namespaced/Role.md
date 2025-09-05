# Role (role)

- Set of permission within a namespace
- Additive rules (there are no "deny" rules)

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: default
rules:
  - apiGroups: [""] # "" indicates the core API group
    resources: ["pods"]
    resourceNames: ["orange-pod", "blue-pod"] # if not specified, pick all
    verbs: ["get", "watch", "list"] # * for all verbs
```
