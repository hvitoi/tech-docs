# eksctl utils

## associate-iam-oidc-provider

- This command creates an `IAM Open ID Connect Provider` for the cluster
- It's useful so that you can use `AWS IAM roles` for `Kubernetes Service Accounts` (IRSA)

```shell
eksctl utils associate-iam-oidc-provider \
  --cluster "foo" \
  --approve
```
