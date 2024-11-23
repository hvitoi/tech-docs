# aws-load-balancer-controller

> This controller is necessary for ALBs only. For CLBs and NLBs this controller is not necessary and the LBs can be created directly from the Service Object

- <https://github.com/kubernetes-sigs/aws-load-balancer-controller>

- AWS Load Balancer Controller (`LBC`) leverages a Kubernetes CRD to manage AWS Elastic Load Balancers (ELBs).
- LBC is composed of kubernetes objects such as `load balancers` and `TargetGroupBindings` that are able to manage `aws resources` (for instance for dynamically creating an ALB)

## IRSA

- LBC requires `IAM Roles for Service Accounts` (IRSA)
- This role is automatically created via eksctl

## Deploy

```shell
set CLUSTER_REGION us-east-1
set CLUSTER_VPC (aws eks describe-cluster --name my-cluster --region $CLUSTER_REGION --query "cluster.resourcesVpcConfig.vpcId" --output text)

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
