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
  - `eksctl-<cluster-name>-nodegroup-<nodegroup-name>`
  - `eksctl-<cluster-name>-addon-aws-ebs-csi-driver`
  - `eksctl-<cluster-name>-addon-iamserviceaccount-kube-system-aws-load-balancer-controller`
  - `eksctl-<cluster-name>-addon-vpc-cni`
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
- The cluster creation may take around 15 minutes

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
  --name "my-node-group" \
  --node-type "t3.medium" \
  --nodes "2" \
  --nodes-min "2" \
  --nodes-max "4" \
  --node-volume-size "20" \ # 20 GiB HDD per node
  --ssh-access \
  --ssh-public-key "my-key-pair" \
  --managed \ # Make it managed worker nodes (aws patches and upgrades it) \
  --node-private-networking \ # deploy the node-group into the private subnet of the EKS cluster

  # addon flags
  --asg-access \ # adds inline policy PolicyAutoScaling to the role of the ec2 instances
  --external-dns-access \ # adds inline policies PolicyExternalDNSHostedZones and PolicyExternalDNSChangeSet to the role of the ec2 instances
  --appmesh-access \ # adds inline policy PolicyAppMesh to the role of the ec2 instances
  --alb-ingress-access \ # adds inline policy PolicyAWSLoadBalancerController to the role of the ec2 instances
  --full-ecr-access # adds managed policies AmazonEC2ContainerRegistryPowerUser and AmazonEC2ContainerRegistryReadOnly to the role of the ec2 instances
```

- The nodegroup creation may take around 5 minutes
- You are able to see the newly created nodes using `kubectl get node`

## addon

```yaml
# Create addons after a cluster has been created
eksctl create addon --config-file=cluster.yaml
```

```shell
set account_id (aws sts get-caller-identity --query Account --output text)
eksctl create addon \
  --name aws-ebs-csi-driver \
  --cluster my-cluster \
  --service-account-role-arn arn:aws:iam::$account_id:role/AmazonEKS_EBS_CSI_DriverRole

eksctl create addon \
  --name eks-pod-identity-agent \
  --version 1.0.0
```

## iamserviceaccount

- Create an `IRSA` (IAM role for service account)
- IRSAs allow Kubernetes resources to manage AWS resources

```shell
eksctl create iamserviceaccount \
  # SA Kubernetes Object name (kubectl get sa/ebs-csi-controller-sa -n kube-system)
  --name ebs-csi-controller-sa \
  # EKS cluster
  --cluster my-cluster \
  # namespace to create the SA
  --namespace kube-system \
  # IAM role name to be created on AWS (can be any name) - If omitted, uses an auto-generated name: eksctl-foo-addon-iamserviceaccount-kube-sys-Role1-9Op08UsCQjpo
  --role-name AmazonEKS_EBS_CSI_DriverRole \
  # policy to attach to the role
  --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
  # do not create the SA (usually when another step will do it)
  --role-only \
  # recreate Kubernetes SAs if they exist already
  --override-existing-serviceaccounts \
  # apply the changes
  --approve
```

## podidentityassociation

```shell
eksctl create podidentityassociation \
  --cluster my-cluster \
  # Namespace where the SA will be created (the app must be deployed in this same namespace)
  --namespace default \
  # SA that will be used for pods to access S3
  --service-account-name s3-app-sa \
  #
  --role-name s3-app-eks-pod-identity-role \
  #
  --permission-policy-arns arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```
