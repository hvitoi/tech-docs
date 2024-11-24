# aws eks

## list-clusters

```shell
aws eks list-clusters --query "clusters[*]" --output text
```

## describe-cluster

- Important Info
  - roleArn (cluster role)
  - vpcId

```shell
aws eks describe-cluster --name foo
```

## list-access-entries

- Describe what iam principals have access to the cluster (including assumable roles)

```shell
aws eks list-access-entries --cluster-name foo
```

## list-access-policies

- List all available policies

```shell
aws eks list-access-policies
```

```txt
AmazonEKSAdminPolicy
AmazonEKSAdminViewPolicy
AmazonEKSClusterAdminPolicy
AmazonEKSEditPolicy
AmazonEKSViewPolicy
AmazonEMRJobPolicy
AmazonSagemakerHyperpodClusterPolicy
AmazonSagemakerHyperpodControllerPolicy
AmazonSagemakerHyperpodSystemNamespacePolicy
```

## update-kubeconfig

```shell
# by cluster name (in the account & region defined in the profile)
aws eks update-kubeconfig --name foo

# Specify another kubeconfig location (other than ~/.kube/config)
aws eks update-kubeconfig \
  --name foo \
  --kubeconfig ~/kubeconfig

# Alias for the context (the cluster remains as the arn)
aws eks update-kubeconfig \
  --name foo \
  --alias my-context

# Alias for the user (the cluster remains as the arn)
aws eks update-kubeconfig \
  --name foo \
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

## describe-addon-versions

- Describe an addon (not necessarily installed in the cluster)

```shell
aws eks describe-addon-versions --addon-name aws-ebs-csi-driver
```

## get-token

- This CLI is usually triggered via kubeconfig so that a get can be fetched on the fly for kubectl

```shell
aws eks get-token --cluster-name foo
```
