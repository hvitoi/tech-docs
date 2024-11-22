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

#### EBS CSI Driver

- Leverages the `Container Storage Interface (CSI)` compliant driver
- Replaces the legacy `In-Tree EBS Provisioner`
- It allows EKS Cluster to `manage lifecycle` of EBS volumes (AWS::EC2::Volume)
- <https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html>

##### IRSA

- `IAM role for service account` (**IRSA**)
- This addon requires permissions to make calls to the AWS API. Otherwise it will fail to create the PVC
- This make it possible to Create a `Persistent Volume Claim (PVC)` managed by k8s itself
- For that the AWS managed policy [AmazonEBSCSIDriverPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEBSCSIDriverPolicy.html) needs to be attached to a new role that will be assumed by the ec2 instance

```shell
# this approach creates a new role (AmazonEKS_EBS_CSI_DriverRole) with the ebs policy (AmazonEBSCSIDriverPolicy) that is assumable by the ec2 instances in the node group
eksctl create iamserviceaccount \
  --name ebs-csi-controller-sa \
  --role-name AmazonEKS_EBS_CSI_DriverRole \
  --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
  --cluster my-cluster \
  --namespace kube-system \
  --role-only \
  --approve
```

- Another option (not recommended) is to attach the ebs policy directly to the ec2 default role (created as part of the node group)

```shell
# Get the ARN policy of the worker nodes
kubectl describe cm/aws-auth -n kube-system

# Attach the ebs policy to the worker node role
aws iam attach-role-policy \
  --role-name "eksctl-henry-nodegroup-my-node-gro-NodeInstanceRole-tZDjAGAMF9gm" \
  --policy-arn "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
```

##### Deploy

```shell
set account_id (aws sts get-caller-identity --query Account --output text)
eksctl create addon \
  --name aws-ebs-csi-driver \
  --cluster my-cluster \
  --service-account-role-arn arn:aws:iam::$account_id:role/AmazonEKS_EBS_CSI_DriverRole
```

```shell
# Verify ebs-csi pods running
kubectl get po -n kube-system

# A "csidrivers" object is created
kubectl get csidrivers
```

- Another option (not recommended) is to deploy the csi objects directly

```shell
kubectl apply -k "github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/?ref=master"
```

##### StorageClass

- After the driver is deployed you need to apply a `StorageClass` with the provisioner `kubernetes.io/aws-ebs` on the cluster
- Then claim the volume (PVC) via the SC, this way a PV will be created automatically
- The EBS volume is created with the name `my-cluster-dynamic-pvc-34bc1e7b-c864-4667-92bd-1141e114297c`

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: ebs-sc
provisioner: ebs.csi.aws.com
volumeBindingMode: WaitForFirstConsumer # waits for the pod to attach the volume for creating it
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  storageClassName: ebs-sc
  resources:
    requests:
      storage: 4Gi # It's the AWS EBS Volume
  accessModes:
    - ReadWriteOnce
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: foo
spec:
  replicas: 1
  strategy:
    type: Recreate
  selector:
    matchLabels:
      app: foo
  template:
    metadata:
      labels:
        app: foo
    spec:
      containers:
        - image: nginx
          name: nginx-container
          volumeMounts:
            - name: my-storage
              mountPath: /mnt
      volumes:
        - name: my-storage
          persistentVolumeClaim:
            claimName: my-pvc
```

#### AWS Load Balancer Controller (LBC)

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

### ServiceAccountRoleArn

- It's the `IAM role for service account` (**IRSA**)
