# RoleBinding

- Grants permissions within a specific namespace

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: henry-developer-binding
  namespace: default # only for resources in this namespace
roleRef: # refer to a role in the current namespace
  apiGroup: rbac.authorization.k8s.io
  kind: Role # Role or ClusterRole
  name: developer # developer Role must be created in the same namespace
subjects:
  - apiGroup: rbac.authorization.k8s.io
    kind: User
    namespace: default # default namespace if not specified
    name: henry # this name comes from the client certificate (CN field)
  - apiGroup: rbac.authorization.k8s.io
    kind: Group
    namespace: default # default namespace if not specified
    name: my-group # this name comes from the client certificate (O field)
  - apiGroup: rbac.authorization.k8s.io
    kind: Group
    namespace: default # default namespace if not specified
    name: e6dsad-2392-ksaj2-92933 # Object ID of the Azure AD Group
```
