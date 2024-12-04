# IAM Principal Authentication

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
