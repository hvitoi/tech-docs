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

- **vpc-cni**
  - Automatically installed

- **coredns**
  - Automatically installed

- **kube-proxy**
  - Automatically installed

- **aws-ebs-csi-driver**
  - Allows Ingress functionalities

- **amazon-cloudwatch-observability**
  - Installs the DaemonSets `cloudwatch-agent`, `fluent-bit` and `neuron-monitor` and the Deploment `cloudwatch-controller`
  - It is installed in the `amazon-cloudwatch` namespace

### ServiceAccountRoleArn

- It's the `IAM role for service account` (**IRSA**)
