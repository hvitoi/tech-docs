# Installation

## Karpenter Resources

- `AWS::IAM::Role`: Role to be used by EC2 instances created by Karpenter
- `AWS::IAM::ManagedPolicy`: Policy to be used by Karpenter to manage EC2 instances
- `AWS::SQS::Queue`: Queue used by Karpenter to schedule the creation of instance
- `AWS::SQS::QueuePolicy`: Policy for the queue
- `AWS::Events::Rule`: Capture aws events and route it to SQS

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
eksctl create cluster -f eks-cluster.yaml

set CLUSTER_ENDPOINT (aws eks describe-cluster --name "my-cluster" --query "cluster.endpoint" --output text)
set KARPENTER_IAM_ROLE_ARN "arn:aws:iam::123456789012:role/my-cluster-karpenter"
```

## Karpenter

```shell
helm registry logout public.ecr.aws

helm upgrade --install karpenter oci://public.ecr.aws/karpenter/karpenter \
  --version "${KARPENTER_VERSION}" \
  --namespace "${KARPENTER_NAMESPACE}" \
  --create-namespace \
  --wait \
  --set "settings.clusterName=${CLUSTER_NAME}" \
  --set "settings.interruptionQueue=${CLUSTER_NAME}" \
  --set controller.resources.requests.cpu=1 \
  --set controller.resources.requests.memory=1Gi \
  --set controller.resources.limits.cpu=1 \
  --set controller.resources.limits.memory=1Gi
```
