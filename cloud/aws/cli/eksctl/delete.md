# eksctl delete

## cluster

- Also deletes the underlying node groups

```shell
# delete by resource
eksctl delete cluster -f eks-cluster.yaml

# delete by cluster name
eksctl delete cluster --name foo
```

## nodegroup

- Delete only the node group

```shell
eksctl delete nodegroup \
  --cluster foo \
  --name my-node-group
```

## fargateprofile

```shell
eksctl delete fargateprofile \
  --cluster foo \
  --name my-fargate-profile \
  --wait
```

## addon

- This will automatically remove any Kubernetes `SA` associated with the addon
- This won't remove IAM roles manually created

```shell
eksctl delete addon \
  --cluster foo \
  --name aws-ebs-csi-driver
```

## iamserviceaccount

- Deletes:
  - The `ServiceAccount`
  - The `IAM Role`

```shell
eksctl delete iamserviceaccount \
  --name ebs-csi-controller-sa \
  --cluster foo \
  --namespace kube-system
```

## podidentityassociation

- Deletes:
  - The `ServiceAccount`
  - The `IAM Role`

```shell
eksctl delete podidentityassociation \
  --cluster foo \
  --namespace kube-system
  --service-account-name aws-load-balancer-controller \
```
