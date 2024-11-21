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

### NodeRole

- It's the role to be assumed by the EC2 instance
- All the pods running in these worker nodes will have the permissions/policies of this role
- This role is automatically created when creating a nodegroup via `eksctl create nodegroup` and the more permissions can be added to the role using the "addon" flags
- ARN example: `arn:aws:iam::123456789012:role/eksctl-henry-nodegroup-my-node-gro-NodeInstanceRole-tZDjAGAMF9gm`
- It's different from the cluster role, which is associated with the control plane

- AWS Managed Policies
  - [AmazonEKSWorkerNodePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKSWorkerNodePolicy.html): allow workers to connect to the EKS cluster
  - [AmazonSSMManagedInstanceCore](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.html): SSM core functionality
  - [AmazonEC2ContainerRegistryReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryReadOnly.html): read access to ECR
  - [AmazonEC2ContainerRegistryPowerUser](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ContainerRegistryPowerUser.html): write access to ECR
  - [AmazonEKS_CNI_Policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKS_CNI_Policy.html): used by the addon "Amazon VPC CNI"

```shell
# describes the config that contains the references to the worker nodes iam role
kubectl describe cm/aws-auth -n kube-system
```
