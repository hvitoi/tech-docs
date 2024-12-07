# eksctl utils

## associate-iam-oidc-provider

- Sets up the `IAM OIDC Provider` as a way to authenticate to the AWS API and associate it with the Kubernetes Cluster
- It's useful so that you can use `AWS IAM roles` for `Kubernetes Service Accounts` (IRSA)

```shell
eksctl utils associate-iam-oidc-provider \
  --cluster "foo" \
  --approve
```
