# AWS::EKS::IdentityProviderConfig

> This is NOT related to the IAM OIDC Provider which is required for IRSA

- Associate an `OIDC provider` as an additional method for user authentication to your Kubernetes cluster.
- After configuring authentication to your cluster you can create Kubernetes `Role` and `ClusterRole` objects, assign permissions to them, and then bind them to the identities using Kubernetes `RoleBinding` and `ClusterRoleBinding` objects

## Authenticating to Kubernetes API

- It's a form of authenticating to the Kubernetes API endpoint
- It requires authentication to your external OIDC provider
- The OIDC provider needs to be previously configured
- With this authentication method you can only interact with the `Kubernetes Objects` but not with AWS resources (e.g., via eksctl)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-identityproviderconfig.html>

```yaml
Type: AWS::EKS::IdentityProviderConfig
Properties:
  ClusterName: String
  IdentityProviderConfigName: String
  Oidc:
    OidcIdentityProviderConfig
  Tags:
    - Tag
  Type: String
```
