# OIDC Provider Authentication

- It's a form of authenticating on the Kubernetes API endpoint
- It requires authentication to your OIDC provider
- The OIDC provider needs to be previously configured
- With this authentication method you can only interact with the `Kubernetes Objects` but not with AWS resources (e.g., via eksctl)
