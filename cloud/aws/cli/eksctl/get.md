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
eksctl get addon --cluster foo
```

## Nodes

### nodegroup

```shell
eksctl get nodegroup --cluster foo
```

### fargateprofile

```shell
eksctl get fargateprofile --cluster foo
```

## Access to AWS

### iamserviceaccount

- Get all SAs em the cluster that are associated with an IAM role

```shell
eksctl get iamserviceaccount --cluster foo
```

### podidentityassociation

```shell
eksctl get podidentityassociation --cluster foo
```

## Access to Kubernetes

### iamidentitymapping

```shell
eksctl get iamidentitymapping --cluster foo
```

### accessentry

```shell
eksctl get accessentry --cluster foo
```

### identityprovider

- Associate an OIDC provider as an additional method for user authentication to your Kubernetes cluster.

```shell
eksctl get identityprovider --cluster foo
```
