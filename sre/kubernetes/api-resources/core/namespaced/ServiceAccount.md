# ServiceAccount (sa)

- <https://kubernetes.io/docs/concepts/security/service-accounts/>
- A service account is a type of `non-human account`
- Entities inside and outside the cluster can use a specific ServiceAccount's credentials
- SAs are different from user accounts
  - By default, user accounts don't exist in the Kubernetes API server; instead, the API server treats user identities as opaque data
  - SAs on the other hand exist as K8S objects in the API server

## Default SA

- Every namespace gets a `default SA` upon creation (which has no permissions by default)
- If you delete the default ServiceAccount object in a namespace, the control plane replaces it with a new one.
- If you deploy a Pod in a namespace, and you don't manually assign a ServiceAccount to the Pod, Kubernetes assigns the default ServiceAccount for that namespace to the Pod.
