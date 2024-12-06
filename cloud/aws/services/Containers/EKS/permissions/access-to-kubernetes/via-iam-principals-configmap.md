# IAM Principal Authentication via ConfigMap

> This authentication method is deprecated, consider using EKS Access Entries to authenticate IAM principals

- It's a form of authenticating on the Kubernetes API endpoint
- It uses an IAM principal (role or user) and therefore you to authenticate to AWS first
- The ability to access your cluster using IAM principals is provided by the [AWS IAM Authenticator for Kubernetes](https://github.com/kubernetes-sigs/aws-iam-authenticator#readme), which runs on the control plane.

```yaml
# ~/.kube/config
users:
- name: henrique.vitoi@foo.us-east-1.eksctl.io
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1beta1
      command: aws
      args:
        - eks
        - get-token
        - --output
        - json
        - --cluster-name
        - foo
        - --region
        - us-east-1
      env:
        - name: AWS_STS_REGIONAL_ENDPOINTS
          value: regional
```

- You can allow IAM principals to access Kubernetes objects on your cluster using `aws-auth ConfigMap` or `Access Entries`

## Initial user

- The `IAM principal` (user or role) that created the cluster is the initial user that can access the cluster by using kubectl
- The initial user must add other users to the list in the `aws-auth` ConfigMap and assign permissions that affect the other users within the cluster.
- These other users can't manage or remove the initial user, as there isn’t an entry in the ConfigMap to manage.

## aws-auth ConfigMap

- <https://docs.aws.amazon.com/eks/latest/userguide/auth-configmap.html>

- This is the original authentication mode for Amazon EKS clusters.
- In this mode the cluster will source `authenticated IAM principals` from the `aws-auth` ConfigMap.

> This authentication method is currently deprecated, consider using EKS Access Entries

```shell
kubectl describe cm/aws-auth -n kube-system
```

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: aws-auth
  namespace: kube-system
data:
  mapRoles: |
    # IAM roles assumed by the worker nodes
    - rolearn: arn:aws:iam::123456789012:role/eksctl-foo-nodegroup-bar-NodeInstanceRole-u4CxYVzWNTmG
      username: system:node:{{EC2PrivateDNSName}} # each nodes's username. E.g., system:node:ip-10-0-0-1.ec2.internal
      groups:
        - system:bootstrappers # Allows nodes to bootstrap themselves.
        - system:nodes # Grants worker nodes permissions needed to function properly.

    # IAM role assumed by CodeBuild (can be migrated into an Access Entry)
    - rolearn: arn:aws:iam::123456789012:role/EksCodeBuildKubectlRole
      username: build
      groups:
        - system:masters # Grants full administrative access to the Kubernetes cluster. Use this group cautiously as it provides extensive permissions.
```
