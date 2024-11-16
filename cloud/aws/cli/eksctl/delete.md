# eksctl delete

```shell
# delete by resource
eksctl delete cluster -f ./eks-cluster.yaml

# delete by cluster name
eksctl delete cluster \
  --region us-west-2 \
  --name my-cluster
```
