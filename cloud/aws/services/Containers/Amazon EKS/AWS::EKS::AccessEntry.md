# AWS::EKS::AccessEntry

- Grants access to Kubernetes Resources by AWS IAM Principals
- Manages `Kubernetes permissions` of `IAM principals` from outside the cluster. Differently from aws-auth that stores the configuration in a ConfigMap stored in the cluster
- It associates an `IAM role` with a `kubernetes entity` (user or group) but this association is not stored in the cluster itself
- You can create and associate access entries with the commands `aws eks create-access-entry` and `aws eks associate-access-policy`, respectively.
