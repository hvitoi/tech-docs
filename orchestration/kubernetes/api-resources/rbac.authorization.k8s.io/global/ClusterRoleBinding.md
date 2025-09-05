# ClusterRoleBinding (clusterrolebinding)

- ClusterRoleBinding grants `permissions cluster-wide`
- Binds a `ClusterRole` to a `ServiceAccount` or `Group`

## Examples

- `cluster-admin`: ClusterRole/cluster-admin
- `system:basic-user`: ClusterRole/system:basic-user

## Properties

### subjects[].kind

#### Group

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

#### ServiceAccount

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: external-dns
rules:
  - apiGroups: [""]
    resources: ["services", "endpoints", "pods"]
    verbs: ["get", "watch", "list"]
  - apiGroups: ["extensions", "networking.k8s.io"]
    resources: ["ingresses"]
    verbs: ["get", "watch", "list"]
  - apiGroups: [""]
    resources: ["nodes"]
    verbs: ["list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: external-dns-viewer
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: external-dns
subjects:
  - kind: ServiceAccount
    name: external-dns
    namespace: default
```
