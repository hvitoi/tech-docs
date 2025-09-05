# kube-scheduler

- Responsible for finding the right node for each container to start on
- The `kube-scheduler` does not deploy the container, but only takes the decision. The deploy itself is performed by the kubelet
- Decision making
  1. `Filter Nodes`: filter nodes which do not match the criteria
  1. `Rank Nodes`: assign a score for the node (from 0 to 10)

## Scheduling Queue

- It's a queue of `pending pods`
- Represent a queue of pods waiting to be assigned to a node

## Scheduling Rules

- **no.spec.taints**: Mark a node with a taint. Only pods with tolerance to this taint can be scheduled to this node
- **po.spec.nodeName**: bypasses kube-scheduler completely and selects a node manually
- **po.spec.NodeSelector**: Schedule a pod to a node based on different criteria
- **po.spec.affinity.nodeAffinity**: A simple node affinity. Schedule based only on a label
- **po.spec.tolerations**: Tolerante of a pod to a node taint
- **po.spec.topologySpreadConstraints**: spread the replicas across AZs

## Setup

### From scratch

- `kube-scheduler.service` must be configured manually if running a kubernetes cluster from scratch

```shell
# Download kube-scheduler binary
wget "https://storage.googleapis.com/kubernetes-release/release/v1.13.0/bin/linux/amd64/kube-scheduler"
```

```conf
ExecStart=/usr/local/bin/kube-scheduler \\
  --scheduler-name=default-scheduler \\ # leave as is for a single scheduler setup
  --config=/etc/kubernetes/config/kube-scheduler.yaml \\
  --leader-elect=true \\ # for multiple masters (multiple replicas of scheduler)
  --v=2
```

- The options can be viewed at `/etc/systemd/system/kube-scheduler.service`
- Or see the running options `px -aux | grep kube-scheduler`

### Via kubeadm

- `kubeadm` install the service automatically as a pod `kube-scheduler` inside of the `kube-system` namespace
- The pod is deployed on the master node

- The options can be viewed at `/etc/kubernetes/manifests/kube-scheduler.yaml`

## Multiple Schedulers

- Multiple scheduler services can run in the cluster
- Modify the `po.spec.schedulerName` property in order to use any other scheduler other than the default one

```conf
ExecStart=/usr/local/bin/kube-scheduler \\
  --scheduler-name=my-custom-scheduler \\
  --config=/etc/kubernetes/config/kube-scheduler.yaml \\
  --leader-elect=true \\
  --lock-object-name=my-custom-scheduler \\
  --v=2
```
