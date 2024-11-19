# AWS::EKS::Addon

## CSI

### EBS CSI Driver

- Leverages the `Container Storage Interface (CSI)` compliant driver
- Replaces the legacy `In-Tree EBS Provisioner`
- It allows EKS Cluster to `manage lifecycle` of EBS volumes

- Need to specify a `StorageClass` manifest on your EKS cluster
- This make it possible to Create a `Persistent Volume Claim (PVC)` managed by k8s itself

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

- It's necessary to create a `IAM role` for the worker nodes, so that they can access the EBS volumes

### EFS CSI Driver

### FSx for Luster CSI Driver

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
