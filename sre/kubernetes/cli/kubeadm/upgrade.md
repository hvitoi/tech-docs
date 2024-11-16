# upgrade

- Upgrades the following components

  - APi Server
  - Controller Manager
  - Scheduler
  - KubeProxy
  - CoreDNS
  - Etcd

- `kubeadm` updates the components of only the node in which it is running, not all the components of the cluster
- `kubeadm` does not upgrade kubelet. It must be upgraded manually
- The version shown in `kubectl get no` is the version of the kubelet of each node

## Master nodes

- **Control Plane**

  ```shell
  # upgrade kubeadm cli
  apt-get upgrade -y "kubeadm=1.21.0-00"
  kubeadm version

  # check which versions are available to upgrade to and validate whether your current cluster is upgradeable
  kubeadm upgrade plan

  # upgrade cluster to a specified version
  kubeadm upgrade apply "1.21.0"
  ```

- **Kubelet**

  ```shell
  # Drain pods in the node
  kubectl drain "master-node" --ignore-daemonsets

  # upgrade kubeadm, kubelet and kubectl
  apt-get upgrade -y "kubelet=1.21.0=00"
  apt-get upgrade -y "kubectl=1.21.0=00"
  systemctl daemon-reload
  systemctl restart kubelet

  # Uncodon the drained node
  kubectl uncordon "master-node"
  ```

## Worker nodes

- **Kubelet**

```shell
# Drain node (must be run from the master node!)
kubectl drain "worker-node" --ignore-daemonsets

# upgrade kubeadm cli
apt-get upgrade -y "kubeadm=1.21.0-00"

# upgrade commands for the node (kubelet version)
kubeadm upgrade node

# upgrade kubelet and kubectl
apt-get upgrade -y "kubelet=1.21.0=00"
apt-get upgrade -y "kubectl=1.21.0=00"
systemctl daemon-reload
systemctl restart kubelet

# Uncodon the drained node (must be run from the master node!)
kubectl uncordon "worker-node"
```
