# IAM roles for service accounts (IRSA)

- <https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html>
- Associates an `IAM Role` with a `Kubernetes Service Account` and configure your Pods to use the SA.
- Allow `Pods` to make requests to `AWS services`

- **Benefits**
  - `Least privilege`: It avoids using the IAM role of the EC2 instances (nodes) and instead use a more granular permission for a specific pod/application
  - `Credential isolation`: a pod's containers can only retrieve credentials for the IAM role that's associated with the SA that the container uses
  - `Auditability`: access and event logging is available

## OIDC Provider

- In order to use IRSAs, you need an `IAM Open ID Connect provider`

```shell
eksctl utils associate-iam-oidc-provider --cluster "my-cluster" --approve
```
