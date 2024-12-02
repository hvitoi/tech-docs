# aws-auth ConfigMap

> The aws-auth ConfigMap is deprecated in favor of EKS access entries

- <https://docs.aws.amazon.com/eks/latest/userguide/auth-configmap.html>
- Access to your cluster using `IAM principals` is enabled by the [AWS IAM Authenticator for Kubernetes](https://github.com/kubernetes-sigs/aws-iam-authenticator#readme), which runs on the Amazon EKS control plane.
- The authenticator gets its configuration information from the `aws-auth ConfigMap`
- `cm/aws-auth` (in the kube-system namespace) is the ConfigMap that contains the references to the IAM roles assumed by the worker nodes

```shell
kubectl describe cm/aws-auth -n kube-system
```

- You can patch the ConfigMap in order to define `multiple roles` depending on the impersonated user
- However, only one role can be used at a time

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: aws-auth
  namespace: kube-system
data:
  mapRoles: |
    - username: system:node:{{EC2PrivateDNSName}} # each nodes's username. E.g., system:node:ip-10-0-0-1.ec2.internal
      rolearn: arn:aws:iam::123456789012:role/eksctl-foo-nodegroup-bar-NodeInstanceRole-u4CxYVzWNTmG
      groups:
        - system:bootstrappers # Allows nodes to bootstrap themselves.
        - system:nodes # Grants worker nodes permissions needed to function properly.
    - username: build
      rolearn: arn:aws:iam::123456789012:role/EksCodeBuildKubectlRole
      groups:
        - system:masters # Grants full administrative access to the Kubernetes cluster. Use this group cautiously as it provides extensive permissions.
```
