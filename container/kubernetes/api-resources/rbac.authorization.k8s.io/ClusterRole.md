# ClusterRole

- Set of permission for the entire cluster

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
  - apiGroups: [""]
    resources: ["secrets"] # grant permissions to all secrets (in all namespaces)
    verbs: ["get", "watch", "list"]
  - apiGroups: [""]
    resources: ["nodes"] # grant permissions to a non-namespaced resource
    verbs: ["list", "get", "create", "delete"],
  - apiGroups: ["", "extensions", "apps"]
    resources: ["*"] # read-only access to all resources in all namespaces
    verbs: ["get", "list", "watch"] # read-only permissions
```
