# AWS::EKS::Addon

- EBS CSI Driver
- EFS CSI Driver
- FSx for Luster CSI Driver

## Properties

```yaml
Type: AWS::EKS::Addon
Properties:
  AddonName: String
  AddonVersion: String
  ClusterName: String
  ConfigurationValues: String
  PodIdentityAssociations:
    - PodIdentityAssociation
  PreserveOnDelete: Boolean
  ResolveConflicts: String
  ServiceAccountRoleArn: String
  Tags:
    - Tag
```

### AddonName

- `vpc-cni`: automatically installed
- `coredns`: automatically installed
- `kube-proxy`: automatically installed
- `aws-ebs-csi-driver`

### ServiceAccountRoleArn

- It's the `IAM role for service account` (**IRSA**)
