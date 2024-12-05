# aws eks

## Cluster

### list-clusters

```shell
aws eks list-clusters --query "clusters[*]" --output text
```

### describe-cluster

- Important Info
  - roleArn (cluster role)
  - vpcId

```shell
aws eks describe-cluster --name foo
```

### update-cluster-config

- Enable `eks access entries` or `aws-auth configmap` authentication with the Kubernetes API

```shell
aws eks update-cluster-config \
  --name my-cluster \
  --access-config authenticationMode=API_AND_CONFIG_MAP
```

## EKS Access Entries

### list-access-policies

- List all `available policies` for EKS Access Entries

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

### list-access-entries

- Describe what `iam principals` (user and roles) have access to the cluster

```shell
aws eks list-access-entries --cluster-name foo
```

### create-access-entry

- The Access Entry is empty at first (no associated policies)

```shell
aws eks create-access-entry \
  --cluster-name my-cluster \
  --principal-arn "arn:aws:iam::123456789012:role/my-role" \
  --type STANDARD \
  --user Viewers \
  --kubernetes-groups Viewers

aws eks create-access-entry \
    --cluster-name my-cluster \
    --principal-arn arn:aws:iam::123456789012:role/fis-experiment-role \
    --username fis-experiment
```

### list-associated-access-policies

- List all policies associated with an Access Entry

```shell
aws eks list-associated-access-policies \
  --cluster-name my-cluster \
  --principal-arn arn:aws:iam::123456789012:role/my-role
```

### associate-access-policy

- Associate an `access policy` to an `access entry`
- Run `aws eks list-access-policies` to get all available policies

```shell
aws eks associate-access-policy \
  --cluster-name my-cluster \
  --principal-arn arn:aws:iam::123456789012:role/my-role \
  --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSViewPolicy \
  --access-scope type=cluster
  # --access-scope type=namespace,namespaces=my-namespace1,my-namespace2
```

## Addons

### describe-addon-versions

- Describe an addon (not necessarily installed in the cluster)

```shell
aws eks describe-addon-versions --addon-name aws-ebs-csi-driver
```

## Setup

### update-kubeconfig

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

### get-token

- This CLI is usually triggered via kubeconfig so that a get can be fetched on the fly for kubectl

```shell
aws eks get-token --cluster-name foo
```
