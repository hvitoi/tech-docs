# AWS::EKS::Nodegroup

- These are the `worker nodes`
- You deploy the worker nodes yourself (with ec2 instances)
- `Node Groups` provision nodes as EC2 that are part of an `Auto Scaling Group (ASG)`
- All instances in a node group must `be the same instance type`, `run the same AMI` and `use the same IAM role (for thw woker node)`

## Resources

- Node Group
  - 1 **Node Group** (AWS::EKS::Nodegroup)

- Template
  - 1 **Launch Template** (AWS::EC2::LaunchTemplate) (`eksctl-foo-nodegroup-bar`)
  - 1 **Autoscaling Group** (AWS::AutoScaling::AutoScalingGroup) (`eks-bar-9ec99b34-480c-d2ac-fca9-68b923c3ecc7`)

- Security
  - 1 **Security Group** (AWS::EC2::SecurityGroup) (SSH: `eksctl-foo-nodegroup-bar/SSH`)
    - For SSH access

- Permissions
  - 1 **IAM Role** (AWS::IAM::Role) (`eksctl-foo-nodegroup-bar-NodeInstanceRole-abcdefghijkl`)
    - To be assumed by the worker nodes (EC2 instances)

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

### NodeRole

- It's the role to be assumed by the EC2 instance. It's used by the AWS resource to access the Kubernetes API and register itself
- All the pods running in these worker nodes will have the permissions/policies of this role
- This role is automatically created when creating a nodegroup via `eksctl create nodegroup` and the more permissions can be added to the role using the "addon" flags
- ARN example: `arn:aws:iam::123456789012:role/eksctl-foo-nodegroup-my-node-gro-NodeInstanceRole-tZDjAGAMF9gm`

- [AmazonEKSWorkerNodePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKSWorkerNodePolicy.html)
  - Added by default
  - Allow workers to connect to the EKS cluster

- [AmazonEC2ContainerRegistryReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryReadOnly.html)
  - Added by default
  - read access to ECR

- [AmazonSSMManagedInstanceCore](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.html)
  - Added by default
  - SSM core functionality

- [AmazonEKS_CNI_Policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKS_CNI_Policy.html)
  - Added by default
  - Used by the addon "Amazon VPC CNI"

### Subnets

- Worker nodes connect to the master nodes (control plane) via the cluster API server endpoint
- It's a good practice to deploy the node group in a `private subnet` (`--node-private-networking` flag in eksctl)
  - For private workers, it should show no `External IP` when running `kubectl get no -o wide`
