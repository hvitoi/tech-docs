# eks

## list-clusters

```shell
aws eks list-clusters --query "clusters[*]" --output text
```

## update-kubeconfig

```shell
# by cluster name (in the account & region defined in the profile)
aws eks update-kubeconfig --name my-cluster

# Specific another kubeconfig location (other than ~/.kube/config)
aws eks update-kubeconfig \
  --name my-cluster \
  --kubeconfig ~/kubeconfig

# Alias for the context (the cluster remains as the arn)
aws eks update-kubeconfig \
  --name my-cluster \
  --alias my-context

# Alias for the user (the cluster remains as the arn)
aws eks update-kubeconfig \
  --name my-cluster \
  --user-alias john
```

```shell
# several clusters
clusters=$(aws eks list-clusters --query "clusters[*]" --output text)
for cluster in $clusters; do
  aws eks update-kubeconfig \
    --name "$cluster" \
    --alias "$cluster"
done
```
