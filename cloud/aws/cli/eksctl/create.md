# eksctl create

## cluster

- <https://docs.aws.amazon.com/eks/latest/userguide/quickstart.html>
- eksctl automatically:
  - Creates a `VPC` for the cluster and create public and private endpoints
  - Creates `IAM roles` (Cluster roles) so that eks can manage itself (e.g., autoscaling)
  - Add `IAM roles` as access entries to the kubernetes cluster, allowing AmazonEKSClusterAdminPolicy to the entity that created the cluster
  - Updates `kubeconfig` with access to your new cluster

- Under the hood some cloudformation templates are created to deploy the cluster and all the requires resources
  - `eksctl-<cluster-name>-cluster`
  - `eksctl-<cluster-name>-addon-aws-ebs-csi-driver`
  - `eksctl-<cluster-name>-addon-iamserviceaccount-kube-system-aws-load-balancer-controller`
  - `eksctl-<cluster-name>-addon-vpc-cni`
  - `eksctl-<cluster-name>-nodegroup-node1`
- Use can follow up the cluster creation on the cloudformation console <https://console.aws.amazon.com/cloudformation>

```shell
# From file
eksctl create cluster -f eks-cluster.yaml

# From params
eksctl create cluster \
  --name "my-cluster" \
  --zones "us-east-1a,us-east-1b" \ # auto-select if unspecified
  --without-nodegroup # no worker nodes (in this case create it manually with eksctl create nodegroup)
```

- Use `aws eks update-kubeconfig` to generate the kubeconfig

## nodegroup

- To create the nodegroup, you need to provide it with a `ssh key pair` for the ec2 instances

```shell
aws ec2 create-key-pair \
  --key-name "my-key-pair" \
  --query 'KeyMaterial' \
  --output text > private-key.pem
```

```shell
eksctl create nodegroup \
  --cluster "my-cluster" \
  --name "my-nodegroup" \
  --node-type "t3.medium" \
  --nodes "2" \
  --nodes-min "2" \
  --nodes-max "4" \
  --node-volume-size "20" \
  --ssh-access \
  --ssh-public-key "my-key-pair" \
  --managed \
  --asg-access \
  --external-dns-access \
  --full-ecr-access \
  --appmesh-access \
  --alb-ingress-access \

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
