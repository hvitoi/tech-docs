# aws-ebs-csi-driver

- <https://github.com/kubernetes-sigs/aws-ebs-csi-driver>
- Leverages the `Container Storage Interface (CSI)` compliant driver
- Replaces the legacy `In-Tree EBS Provisioner`
- It allows EKS Cluster to `manage lifecycle` of EBS volumes (AWS::EC2::Volume)
- <https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html>

## Permissions

### IRSA

- The controller runs on the worker nodes, so it needs access to the `AWS EBS` APIs with IAM permissions
- The IAM permissions can either be setup using `IAM roles for service accounts (IRSA)` (preferred) or can be attached directly to the `worker node IAM roles`

- AWS managed policy: [AmazonEBSCSIDriverPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEBSCSIDriverPolicy.html)

```shell
# Create an OIDC provider
eksctl utils associate-iam-oidc-provider --cluster=attractive-gopher --approve

# Create IRSA
eksctl create iamserviceaccount \
  --name ebs-csi-controller-sa \
  --cluster foo \
  --namespace kube-system \
  --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
  --approve
```

### Node Role

- Another option (not recommended) is to attach the ebs policy directly to the role of the ec2 instances of the worker nodes

```shell
# Get the ARN policy of the worker nodes
kubectl describe cm/aws-auth -n kube-system

# Attach the ebs policy to the worker node role
aws iam attach-role-policy \
  --role-name "eksctl-henry-nodegroup-my-node-gro-NodeInstanceRole-tZDjAGAMF9gm" \
  --policy-arn "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
```

## Installation

```shell
set account_id (aws sts get-caller-identity --query Account --output text)
eksctl create addon \
  --name aws-ebs-csi-driver \
  --cluster foo \
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

## Kubernetes Objects

- After the driver is deployed you need to apply a `StorageClass` with the provisioner `kubernetes.io/aws-ebs` on the cluster
- Then claim the volume (PVC) via the SC, this way a PV will be created automatically
- The EBS volume is created with the name `foo-dynamic-pvc-34bc1e7b-c864-4667-92bd-1141e114297c`

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
