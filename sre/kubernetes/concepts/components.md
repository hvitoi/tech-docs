# Kubernetes

- <https://kubernetes.io/docs/concepts/overview/components/>

- A Kubernetes cluster has two types of nodes (virtual machines)
  - `Worker nodes`: host the containers and the workloads
  - `Master nodes`: it's the controller
    - _Manage_, _plan_, _schedule_, _monitor_ the worker nodes.
    - It receives the instructions from the config file.
    - Master node has the control plane components

![Kubernetes Components](.images/kubernetes-components.svg)

## Control Plane (Master Nodes)

- The control plane is deployed in the master nodes
- Control plane components are deployed as `static pods` on each master node (that means there are 4 manifests in /etc/kubernetes/manifests)

- **etcd**: k8s.gcr.io/etcd:3.4.13-0
- **kube-apiserver**: k8s.gcr.io/kube-apiserver:v1.21.2
- **kube-controller-manager**: k8s.gcr.io/kube-controller-manager:v1.21.2
- **kube-scheduler**: k8s.gcr.io/kube-scheduler:v1.21.2

## Data Plane (Worker Nodes)

- These components are deployed in every cluster node (master or worker)

- **kubelet**: deployed manually as a Service
- **kube-proxy**: deployed as a DaemonSet
- **container runtime**
