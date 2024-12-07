# IAM roles for service accounts (IRSA)

- <https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html>
- Associates an `IAM Role` with a `Kubernetes ServiceAccount` and configure your Pods to use the SA.
- Allow `Pods` to make requests to `AWS services`
- It is possible to associate the same IAM Role to multiple Kubernetes ServiceAccounts

- **Benefits**
  - `Least privilege`: It avoids using the IAM role of the EC2 instances (nodes) and instead use a more granular permission for a specific pod/application
  - `Credential isolation`: a pod's containers can only retrieve credentials for the IAM role that's associated with the SA that the container uses
  - `Auditability`: access and event logging is available

## IAM OIDC provider

> Do not confuse it with the external OIDC provider required for authentication to the Kubernetes API

- In order to use IRSAs, you need associate your cluster with the `IAM OIDC Provider` (associate it with `eksctl utils associate-iam-oidc-provider`)
- This allows IAM to authenticate kubernetes workloads/pods to AWS API using IRSAs.

## Association

- Use the command `eksctl create iamserviceaccount` to create the association between `IAM Role` and `Service Account`

### IAM Role - Trust Policy

> The IAM role with this trust policy is automatically created with "eksctl create iamserviceaccount"

- The `IAM Role` has a Trust Policy document so that the role can be used only by the corresponding SA

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/0123456789ABCDEF0123456789ABCDEF"
      },
      "Condition": {
        "StringEquals": {
          "oidc.eks.us-east-1.amazonaws.com/id/7B4887CC1B7841B1BAEB98263BC64B9C:aud": "sts.amazonaws.com",
          "oidc.eks.us-east-1.amazonaws.com/id/7B4887CC1B7841B1BAEB98263BC64B9C:sub": "system:serviceaccount:kube-system:aws-load-balancer-controller"
        }
      }
    }
  ]
}
```

### Service Account - Annotation

> The Service Account with this annotation is automatically created with "eksctl create iamserviceaccount"

- `SA` are annotated so that they are associated with the IAM role
- The `SA` is "empty" and all the permissions are described in the IAM role

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::307096125112:role/eksctl-foo-addon-iamserviceaccount-kube-sys-Role1-9Op08UsCQjpo
  name: aws-load-balancer-controller
  namespace: kube-system
```
