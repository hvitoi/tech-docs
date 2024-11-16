# AWS::EKS::Nodegroup

- These are the `worker nodes`
- You deploy the worker nodes yourself (with ec2 instances)
- `Node Groups` provision nodes as EC2 that are part of an `Auto Scaling Group (ASG)`
- All instances in a node group must `be the same instance type`, `run the same AMI` and `use the same IAM role (for thw woker node)`
- Worker nodes connect to the master nodes (control plane) via the cluster API server endpoint

## Properties

```yaml
Type: AWS::EKS::Nodegroup
Properties:
  AmiType: String
  CapacityType: String
  ClusterName: String
  DiskSize: Integer
  ForceUpdateEnabled: Boolean
  InstanceTypes:
    - String
  Labels:
    Key: Value
  LaunchTemplate:
    LaunchTemplateSpecification
  NodegroupName: String
  NodeRole: String
  ReleaseVersion: String
  RemoteAccess:
    RemoteAccess
  ScalingConfig:
    ScalingConfig
  Subnets:
    - String
  Tags:
    Key: Value
  Taints:
    - Taint
  UpdateConfig:
    UpdateConfig
  Version: String
```

### CapacityType

- `ON_DEMAND`
- `SPOT`
- `CAPACITY_BLOCK`
