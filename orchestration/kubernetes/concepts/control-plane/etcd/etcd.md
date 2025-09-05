# etcd

- It's a distributed `key-value database`
- It is the `backing store` for all the Kubernetes cluster data
- It stores the `desired state`
- Maintain information about the worker nodes
  - E.g., what containers were deployed at what time
- Stores information regarding the cluster such as
  - Nodes, pods, configs, secrets, accounts, roles, binding, others
- Every information got from kubectl comes from etcd
- You must specify the path to certificate files so that etcdctl can authenticate to `etcd API Server`
