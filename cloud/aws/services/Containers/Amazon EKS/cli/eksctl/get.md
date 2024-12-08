# eksctl get

## cluster

```shell
eksctl get cluster
```

## addon

- Lists all addons installed in the cluster
- Examples
  - kube-proxy
  - coredns
  - vpc-cni
  - aws-ebs-csi-driver

```shell
eksctl get addon --cluster my-cluster
```

## Nodes

### nodegroup

```shell
eksctl get nodegroup --cluster my-cluster
```

### fargateprofile

```shell
eksctl get fargateprofile --cluster my-cluster
```

## Access to AWS

### iamserviceaccount

- Get all SAs em the cluster that are associated with an IAM role

```shell
eksctl get iamserviceaccount --cluster my-cluster
```

### podidentityassociation

```shell
eksctl get podidentityassociation --cluster my-cluster
```

## Access to Kubernetes

### iamidentitymapping

```shell
eksctl get iamidentitymapping --cluster my-cluster
```

### accessentry

```shell
eksctl get accessentry --cluster my-cluster
```

### identityprovider

- The the `external` OIDC providers used as an additional method for user authentication to the cluster

```shell
eksctl get identityprovider --cluster my-cluster
```
