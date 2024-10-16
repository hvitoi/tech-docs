# eks

## list-clusters

```shell
aws eks list-clusters --query "clusters[*]" --output text
```

## update-kubeconfig

```shell
clusters=$(aws eks list-clusters --query "clusters[*]" --output text)

for cluster in $clusters; do
  aws eks update-kubeconfig --name "$cluster"
done
```
