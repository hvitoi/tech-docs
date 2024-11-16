# eksctl utils

## associate-iam-oidc-provider

- This command creates an `IAM Open ID Connect provider` for the cluster
- It's useful so that you can use `AWS IAM roles` for `Kubernetes Service Accounts`

```shell
eksctl utils associate-iam-oidc-provider \
  --cluster "my-cluster" \
  --approve
```
