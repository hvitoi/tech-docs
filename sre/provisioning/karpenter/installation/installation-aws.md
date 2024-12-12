# Installation

## Karpenter AWS Resources

- `AWS::IAM::Role`: Role to be used by EC2 instances created by Karpenter
- `AWS::IAM::ManagedPolicy`: Policy to be used by the Karpenter Controller to manage EC2 instances (The role with this policy is created as part of the PodIdentity resource)
- `AWS::SQS::Queue`: Queue used by Karpenter for interruption
- `AWS::SQS::QueuePolicy`: Policy for the above queue
- `AWS::Events::Rule`: Capture aws events (from event bridge) and route it to SQS

```shell
# Get the latest roles config
curl -fsSL https://raw.githubusercontent.com/aws/karpenter-provider-aws/v1.1.0/website/content/en/preview/getting-started/getting-started-with-karpenter/cloudformation.yaml > karpenter-infra.yaml

# Deploy
aws cloudformation deploy \
  --stack-name "Karpenter-my-cluster" \
  --template-file karpenter-infra.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides "ClusterName=my-cluster"
```

## EKS Cluster

```shell
# Create a cluster from scratch
eksctl create cluster -f eks-cluster.yaml
```

... Or configure an existing cluster (requires the eks-pod-identity-agent addon)

```shell
# Create PodIdentity (permission to the Karpenter controller to manage AWS)
# It creates a new role with the policy defined in Karpenter resources
# The ServiceAccount itself will be created when deploying Karpenter K8S manifests
eksctl create podidentityassociation \
  --cluster my-cluster \
  --service-account-name karpenter \
  --namespace kube-system \
  --role-name my-cluster-karpenter \
  --permission-policy-arns arn:aws:iam::123456789012:policy/KarpenterControllerPolicy-my-cluster
```

```shell
# Create IAM Identity Map via aws-auth (permission to the EC2 instances to register itself in Kubernetes)
# It creates an entry in aws-auth ConfigMap and uses the role define in Karpenter resources
eksctl create iamidentitymapping \
  --cluster my-cluster \
  --arn "arn:aws:iam::123456789012:role/KarpenterNodeRole-my-cluster" \
  --username "system:node:{{EC2PrivateDNSName}}" \
  --group "system:bootstrappers,system:nodes"
```

## Karpenter Kubernetes Controller

```shell
helm registry logout public.ecr.aws

helm upgrade karpenter oci://public.ecr.aws/karpenter/karpenter \
  --install \
  --namespace "kube-system" \
  --wait \
  --set "settings.clusterName=my-cluster" \
  --set "settings.interruptionQueue=my-cluster" \
  --set controller.resources.requests.cpu=1 \
  --set controller.resources.requests.memory=1Gi \
  --set controller.resources.limits.cpu=1 \
  --set controller.resources.limits.memory=1Gi
```

## Karpenter Kubernetes Resources

```shell
kubectl apply -f k8s-manifests.yaml
kubectl describe ec2nc/default
kubectl describe nodepools/default
```
