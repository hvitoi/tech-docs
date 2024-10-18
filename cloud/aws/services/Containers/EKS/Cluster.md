# AWS::EKS::Cluster

- `Elastic Kubernetes Service`
- Container orchestration
- It's an alternative to ECS

![EKS](.images/eks.png)

- **Modes**
  - `EC2 Launch Mode`: you deploy the worker nodes yourself (with ec2 instances)
  - `Fargate Mode`: fully managed and serverless

## Node Types

- `Managed Node Groups`
  - AWS  will create and manage EC2 instances for you
  - Nodes are part of an Auto Scaling Group (ASG) managed by EKS
  - Support `On-demand instances` or `Spot instances`
- `Self-managed Nodes`
  - Nodes created by you and registered to EKS
- `AWS Fargate`
  - No maintenance required.
  - No EC2, no managed nodes. All abstracted away
- `Karpenter`

## AWS Load Balancer Controller (LBC)

- AWS Load Balancer Controller (`LBC`) leverages a Kubernetes CRD to manage AWS Elastic Load Balancers (ELBs).
- LBC is composed of kubernetes objects such as `load balancers` and `TargetGroupBindings` that are able to manage `aws resources` (for instance for dynamically creating an ALB)

> LBC requires IAM Roles for Service Accounts (IRSA). This role is automatically created via eksctl

```shell
export CLUSTER_REGION=us-east-1
export CLUSTER_VPC=$(aws eks describe-cluster --name web-quickstart --region $CLUSTER_REGION --query "cluster.resourcesVpcConfig.vpcId" --output text)

helm repo add eks https://aws.github.io/eks-charts
helm repo update eks
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
    --namespace kube-system \
    --set clusterName=my-cluster \
    --set serviceAccount.create=false \
    --set region=${CLUSTER_REGION} \
    --set vpcId=${CLUSTER_VPC} \
    --set serviceAccount.name=aws-load-balancer-controller # the IAM Roles for Service Accounts (IRSA) created beforehand
```

## Amazon EBS CSI Driver

- Leverages the `Container Storage Interface (CSI)` compliant driver
- Need to specify a `StorageClass` manifest on your EKS cluster
- This make it possible to Create a `Persistent Volume Claim (PVC)` managed by k8s itself
- Storage Support
  - EBS
  - EFS
  - FSx for Lustre
  - FSx for NetApp ONTAP

- With eksctl, it's created as an addon

```yaml
addons:
  - name: aws-ebs-csi-driver
    wellKnownPolicies:
      ebsCSIController: true
```

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: game-data-pvc
spec:
  storageClassName: ebs-sc
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

## Deploy an application

- This creates
  - An application (deployment + service) named service-2048 that exposes the deployment on port 80
  - An Ingress resource named ingress-2048 that defines routing rules for incoming HTTP traffic and annotations for an internet-facing ALB

```shell
# 2048 game
kubectl create namespace game-2048 --save-config
kubectl apply -n game-2048 -f https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.8.0/docs/examples/2048/2048_full.yaml
```

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

- The role that provides permissions for the `Kubernetes control plane` to make `calls to AWS API operations on your behalf`
- The `Cluster IAM role` is important for the cluster to auto-manage itself. Example: to create more nodes (ec2 instances) when scaling is needed
- The cluster role must be associated with a policy that allow managing several aspects of aws

```json
// AmazonEKSClusterPolicy
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "autoscaling:DescribeAutoScalingGroups",
        "ec2:AttachVolume",
        "elasticloadbalancing:AddTags",
        "kms:DescribeKey",
        ...
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "iam:AWSServiceName": "elasticloadbalancing.amazonaws.com"
        }
      }
    }
  ]
}
```
