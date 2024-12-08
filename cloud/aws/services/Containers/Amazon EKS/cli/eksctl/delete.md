# eksctl delete

## cluster

- Also deletes the underlying node groups

```shell
# delete by resource
eksctl delete cluster -f eks-cluster.yaml

# delete by cluster name
eksctl delete cluster --name my-cluster
```

## addon

- This will automatically remove any Kubernetes `SA` associated with the addon
- This won't remove IAM roles manually created

```shell
eksctl delete addon \
  --cluster my-cluster \
  --name aws-ebs-csi-driver
```

## Nodes

### nodegroup

- Delete only the node group

```shell
eksctl delete nodegroup \
  --cluster my-cluster \
  --name my-node-group
```

### fargateprofile

```shell
eksctl delete fargateprofile \
  --cluster my-cluster \
  --name my-fargate-profile \
  --wait
```

## Access to AWS

### iamserviceaccount

- Deletes:
  - The `ServiceAccount`
  - The `IAM Role`

```shell
eksctl delete iamserviceaccount \
  --name ebs-csi-controller-sa \
  --cluster my-cluster \
  --namespace kube-system
```

### podidentityassociation

- Deletes:
  - The `ServiceAccount`
  - The `IAM Role`

```shell
eksctl delete podidentityassociation \
  --cluster my-cluster \
  --namespace kube-system
  --service-account-name aws-load-balancer-controller \
```

## Access to Kubernetes

### iamidentitymapping

```shell
eksctl delete iamidentitymapping \
  --cluster my-cluster \
  --arn "arn:aws:iam::123456789012:role/<role>"
```

### accessentry

```shell
eksctl delete accessentry \
  --cluster my-cluster \
  --principal-arn <arn>
```
