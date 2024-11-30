# eksctl create

## cluster

- <https://docs.aws.amazon.com/eks/latest/userguide/quickstart.html>
- Use can follow up the cluster creation on the cloudformation console <https://console.aws.amazon.com/cloudformation>
- Under the hood some cloudformation templates are created to deploy the cluster and all the requires resources
  - `eksctl-<cluster-name>-cluster`
  - `eksctl-<cluster-name>-nodegroup-<nodegroup-name>`
  - `eksctl-<cluster-name>-addon-<addon-name>`

```shell
# From file
eksctl create cluster -f eks-cluster.yaml

# From params
eksctl create cluster \
  --name foo \
  --without-nodegroup # no worker nodes (in this case create it manually with eksctl create nodegroup)
```

- This automatically adds your role (that created the cluster) as a `AmazonEKSClusterAdminPolicy`
- The kubeconfig should be configured by eksctl but you can also run `aws eks update-kubeconfig`

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
  --cluster foo \
  --name my-node-group \

  # node group
  --node-type t3.medium \
  --nodes "2" \
  --nodes-min "2" \
  --nodes-max "4" \
  # 20 GiB HDD per node
  --node-volume-size "20" \
  --ssh-access \
  --ssh-public-key "my-key-pair" \
  # Make it managed worker nodes (aws patches and upgrades it) \
  --managed \
  # deploy the node-group into the private subnet of the EKS cluster
  --node-private-networking \

  # adds inline policy PolicyAutoScaling to the role of the ec2 instances
  --asg-access \
  # adds inline policies PolicyExternalDNSHostedZones and PolicyExternalDNSChangeSet to the role of the ec2 instances
  --external-dns-access \
  # adds inline policy PolicyAppMesh to the role of the ec2 instances
  --appmesh-access \
  # adds inline policy PolicyAWSLoadBalancerController to the role of the ec2 instances
  --alb-ingress-access \
  # adds managed policies AmazonEC2ContainerRegistryPowerUser and AmazonEC2ContainerRegistryReadOnly to the role of the ec2 instances
  --full-ecr-access
```

- The nodegroup creation may take around 5 minutes
- You are able to see the newly created nodes using `kubectl get node`

## fargateprofile

```shell
eksctl create fargateprofile \
  --cluster foo \
  --name my-fargate-profile \
  --namespace my-fargate-ns # all pods deployed to this ns will be scheduled to this fargate profiles
```

## addon

```shell
# Create addons after a cluster has been created
eksctl create addon --config-file cluster.yaml
```

```shell
set account_id (aws sts get-caller-identity --query Account --output text)
eksctl create addon \
  --name aws-ebs-csi-driver \
  --cluster foo \
  --service-account-role-arn arn:aws:iam::$account_id:role/AmazonEKS_EBS_CSI_DriverRole

eksctl create addon \
  --name eks-pod-identity-agent \
  --cluster foo \
  --version 1.0.0
```

## iamserviceaccount

- Create an `IRSA` (IAM role for service account)
- IRSAs allow Kubernetes resources to manage AWS resources
- This creates a CloudFormation stack with the name like `eksctl-foo-addon-iamserviceaccount-<namespace>-<sa-name>`

```shell
eksctl create iamserviceaccount \
  # SA Kubernetes Object name (kubectl get sa/ebs-csi-controller-sa -n kube-system) to be created
  --name ebs-csi-controller-sa \
  # EKS cluster
  --cluster foo \
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

- Creates a CloudFormation stack `eksctl-<cluster>-podidentityrole-<namespace>-<sa-name>`
- Uses the API `CreatePodIdentityAssociation`

```shell
eksctl create podidentityassociation \
  # cluster name
  --cluster foo \
  # Namespace where the SA will be created (the app must be deployed in this same namespace)
  --namespace default \
  # SA to be created (it will be used by pods to access AWS resources)
  --service-account-name s3-app-sa \
  # Create SA in the cluster (not created by default)
  --create-service-account \

  # IAM role to be created (if omitted uses an auto-generated name)
  --role-name s3-app-eks-pod-identity-role \
  # The policy to attach to the role
  --permission-policy-arns arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```
