# Role

- Set of permission within a namespace
- Additive rules (there are no "deny" rules)

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
  namespace: default
rules:
  - apiGroups: [""] # "" indicates the core API group (po, svc, etc)
    resources: ["pods"]
    verbs: ["list", "get", "create", "update", "delete"]
    resourceNames: ["orange-pod", "blue-pod"] # if not specified, pick all
  - apiGroups: [""]
    resources: ["ConfigMaps"]
    verbs: ["create"]
  - apiGroups: ["batch"]
    resources: ["jobs", "cronjobs"]
    verbs: ["*"]
```
