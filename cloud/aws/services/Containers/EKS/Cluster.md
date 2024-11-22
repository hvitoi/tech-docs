# AWS::EKS::Cluster

- `Elastic Kubernetes Service` is a container orchestration service
- It's an alternative to ECS
- ARN example: `arn:aws:eks:us-east-1:123456789012:cluster/henry`

![EKS](.images/eks.png)
![EKS Components](.images/eks-components.png)

- EKS Cluster outputs:
  - API server endpoint `https://0123456789ABCDEF0123456789ABCDEF.gr7.us-east-1.eks.amazonaws.com`
  - OpenID Connect provider URL `https://oidc.eks.us-east-1.amazonaws.com/id/0123456789ABCDEF0123456789ABCDEF`
  - Cluster IAM role ARN `arn:aws:iam::123456789012:role/eksctl-henry-cluster-ServiceRole-VBrrsaRBhVBQ`

## Control Plane

- Created by the resource AWS::EKS::Cluster (this resource)
- Contains the `master components` (etcd, kube-apiserver, kube-controller, etc)
  - 2 API servers & 3 etc nodes that run across 3 AZs
- It's managed by AWS. The control plane nodes are not shown in `kubectl get node`

- As part of the creation of the cluster a set of network components are created, including a `VPC`
  - Restrict networking traffic between control plane components
  - Control plane components cannot communicate with other aws resources except as authorized via RBAC

## Worker Nodes

- **Node Groups** (EC2 Launch Mode)
  - Created by the resource AWS::EKS::Nodegroup
  - Worker nodes baked by EC2 instances

- **Fargate Profiles** (Fargate Mode)
  - Created by the resource AWS::EKS::FargateProfile

- **Self-managed Nodes**
  - Nodes created by you and registered to EKS

- **Karpenter**

## Pricing

- Control Plane
  - `$0.10 / hour`, `$2.40 / day`, `$72 / month`

- Node Groups
  - Depends on the types and number of EC2 instances used
  - E.g., t3.medium: `$30 / month`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html>

```yaml
Type: AWS::EKS::Cluster
Properties:
  AccessConfig:
    AccessConfig
  BootstrapSelfManagedAddons: Boolean
  EncryptionConfig:
    - EncryptionConfig
  KubernetesNetworkConfig:
    KubernetesNetworkConfig
  Logging:
    Logging
  Name: String
  OutpostConfig:
    OutpostConfig
  ResourcesVpcConfig:
    ResourcesVpcConfig
  RoleArn: String
  Tags:
    - Tag
  UpgradePolicy:
    UpgradePolicy
  Version: String
  ZonalShiftConfig:
    ZonalShiftConfig
```

### RoleArn

- It's the `Cluster IAM role`
- This role that provides permissions for the `Kubernetes control plane` to make `calls to AWS API operations on your behalf`
- This role is important for the cluster to auto-manage itself. Example: to create more nodes (ec2 instances) when scaling is needed
- The cluster role must be associated with a policy that allow managing several aspects of aws
- ARN example: `arn:aws:iam::123456789012:role/eksctl-henry-cluster-ServiceRole-VBrrsaRBhVBQ`
- It's different from the node group role, which is attached to the worker nodes

- Managed Policies
  - [AmazonEKSClusterPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKSClusterPolicy.html)
  - [AmazonEKSVPCResourceController](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKSVPCResourceController.html)
