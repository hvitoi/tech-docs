# kubelet

- kubelet is the agent that runs on each node of the cluster (workers and masters)
- `Attributions`
  - Register a new node within the Kubernetes cluster
  - Create pods
  - Monitor nodes & pods (ensure it's running properly)

- It listens instructions from the API server (E.g, deploy, destroy containers)
- kube-apiserver periodically fetches `status report` from the kubelet

## Static Pods

- `kubelet` continues to function even without the master node or any other worker nodes
- Without a master node, it has node connection with the kube-apiserver and therefore cannot receive instructions
- The kubelet can however create `static pods` by constantly reading manifests from a local directory `/etc/kubernetes/manifests`
  - This path is defined by the `pod-manifest-path` parameter
  - Or by specifying it in the `config.yaml` file (defined in the `config` parameter) with the `staticPodPath` option
- Static pods are also `mirrored` as objects in the kube-apiserver.
  - Mirrored objects are read-only and cannot be updated or deleted
  - Static pods can only be modified by means of the manifest folder
- Static pods are used to deploy the `control plane components` itself. As pods! (not conventional services). That's how kubeadm set up the cluster
  - That's why pods in `kube-system` namespace are shown, they are only mirrors to static the pods
