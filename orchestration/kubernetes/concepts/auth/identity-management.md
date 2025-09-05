# Identity Management

- Kubernetes is designed to separate `identity management` from `access control`.
- It relies on external systems for user authentication, focusing only on authorization (e.g., RBAC with `Role`, `RoleBinding`, `ClusterRole`, `ClusterRoleBinding`).
- Thus, `Users` are not Kubernetes-native objects but are referenced within RBAC rules for authorization purposes.

## User and Groups

- Users are not created or managed directly by Kubernetes. Instead:
  - They are defined and authenticated via an external system, such as certificates, tokens, or an identity provider (e.g., OAuth, LDAP).
  - For example, if you're using client certificates, the "User" is determined by the `Common Name (CN)` field in the certificate.

- You can create a "user" using a certificate

```shell
# Generate a private key
openssl genrsa -out henry.key 2048

# Generate a certificate signing request (CSR).
openssl req -new -key henry.key -out henry.csr -subj "/CN=henry/O=my-group"

# Sign the CSR with the Kubernetes cluster's Certificate Authority (CA).
openssl x509 -req -in henry.csr -CA /path/to/ca.crt -CAkey /path/to/ca.key -CAcreateserial -out henry.crt -days 365

# Use the signed certificate to authenticate to the cluster!
```

## See your users

- You can still see the "users" interfacing with your cluster in form of `RoleBinding` or `ClusterRoleBinding`

```shell
kubectl get rolebindings,clusterrolebindings -A
```
