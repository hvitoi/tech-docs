# create

## cluster

- Use `aws eks update-kubeconfig` beforeto configure the kubeconfig
- eksctl automatically creates
  - A `VPC` for the cluster and create public and private endpoints
  - Cluster roles (arn:aws:iam::my-account:role)
- Under the hood it creates a cloudformation template to deploy the cluster and all the requires resources. The name of the cloudformation resource is `eksctl-<cluster-name>-cluster`

```shell
eksctl create cluster -f eks-cluster.yaml
```

```yaml
# eks-cluster.yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: my-cluster
  version: "1.30"
  region: us-west-2

managedNodeGroups:
  - name: spot
    instanceTypes: ["t3.medium"]
    desiredCapacity: 1
    volumeSize: 80
    spot: true

  - name: spot-2
    instanceTypes: ["t3.small"]
    desiredCapacity: 1
    volumeSize: 80
    spot: true

  # On-Demand instances
  - name: on-demand
    instanceTypes: ["t3.small", "t3.medium"]
    desiredCapacity: 1
    volumeSize: 80
```

## iamserviceaccount

```shell
eksctl create iamserviceaccount \
  --region us-west-2 \
  --cluster my-cluster \
  --namespace kube-system \
  --name ebs-csi-controller-sa \
  --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
  --approve \
  --role-only \
  --role-name AmazonEKS_EBS_CSI_DriverRole
```

## addon

```shell
account_id=$(aws sts get-caller-identity --query Account --output text --profile=dev-prod)

eksctl create addon \
  --region us-west-2 \
  --cluster my-cluster \
  --name aws-ebs-csi-driver \
  --service-account-role-arn arn:aws:iam::$account_id:role/AmazonEKS_EBS_CSI_DriverRole \
  --force
```
