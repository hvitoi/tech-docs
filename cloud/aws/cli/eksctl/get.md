# eksctl get

## cluster

```shell
eksctl get cluster
```

## nodegroup

```shell
eksctl get nodegroup --cluster my-cluster
```

## iamserviceaccount

```shell
eksctl get iamserviceaccount --cluster my-cluster
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
