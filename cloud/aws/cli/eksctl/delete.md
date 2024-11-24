# eksctl delete

## cluster

- Also deletes the underlying node groups

```shell
# delete by resource
eksctl delete cluster -f ./eks-cluster.yaml

# delete by cluster name
eksctl delete cluster \
  --region us-west-2 \
  --name my-cluster
```

## nodegroup

- Delete only the node group

```shell
eksctl delete nodegroup \
  --cluster "my-cluster" \
  --name "my-node-group"
```

## addon

- This will automatically remove any Kubernetes `SA` associated with the addon
- This won't remove IAM roles manually created

```shell
eksctl delete addon \
  --cluster "my-cluster" \
  --name "aws-ebs-csi-driver"
```

## iamserviceaccount

- Deletes:
  - The `ServiceAccount`
  - The `IAM Role`

```shell
eksctl delete iamserviceaccount \
  --name ebs-csi-controller-sa \
  --cluster henry \
  --namespace kube-system
```

## podidentityassociation

- Deletes:
  - The `ServiceAccount`
  - The `IAM Role`

```shell
eksctl delete podidentityassociation \
  --service-account-name aws-load-balancer-controller \
  --cluster henry \
  --namespace kube-system
```
