# ClusterRoleBinding

- ClusterRoleBinding grants that access cluster-wide

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: read-secrets-global
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: secret-reader
subjects:
  - apiGroup: rbac.authorization.k8s.io
    kind: Group
    name: manager # grant the role to all users in this group
```
