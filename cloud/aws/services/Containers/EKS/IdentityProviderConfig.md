# AWS::EKS::IdentityProviderConfig

- Associates an identity provider configuration to a cluster.
- If you want to `authenticate identities` using an `identity provider`, you can create an `identity provider configuration` and associate it to your cluster.
- After configuring authentication to your cluster you can create Kubernetes `Role` and `ClusterRole` objects, assign permissions to them, and then bind them to the identities using Kubernetes `RoleBinding` and `ClusterRoleBinding` objects

## OIDC Provider for authenticating to AWS API

- In order authenticate kubernetes workloads to AWS API using IRSAs, you need an `IAM Open ID Connect provider`
- This is what makes your EKS CLuster as an Identity Provider that is able to tell (based on the `identity information` contained in the SA and its association with pods) what pods can access certain AWS resources
- Use the command `eksctl utils associate-iam-oidc-provider` to create it

## OIDC Provider for authenticating to Kubernetes API

- It's a form of authenticating on the Kubernetes API endpoint
- It requires authentication to your OIDC provider
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
