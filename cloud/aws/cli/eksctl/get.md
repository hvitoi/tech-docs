# eksctl get

## cluster

```shell
eksctl get cluster
```

## nodegroup

```shell
eksctl get nodegroup --cluster foo
```

## iamserviceaccount

- Get all SAs em the cluster that are associated with an IAM role

```shell
eksctl get iamserviceaccount --cluster foo
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
