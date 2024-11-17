# Setup

- `Kubelet` can only be installed manually! kubeadm does not install kubelet on worker nodes
- `kubelet.service` must be configured

```shell
# Download kubelet binary
wget "https://storage.googleapis.com/kubernetes-release/release/v1.13.0/bin/linux/amd64/kubelet"
```

```conf
ExecStart=/usr/local/bin/kubelet \\
  --config=/var/lib/kubelet/config.yaml \\
  --container-runtime=remote \\
  --container-runtime-endpoint=unix:///var/run/containerd/containerd/sock \\
  --pod-manifest-path=/etc/kubernetes/manifests \\
  --image-pull-progress-deadline=2m \\
  --kubeconfig=/var/lib/kubelet/kubeconfig \\
  --network-plugin=cni \\ # CNI
  --cni-conf-dir=/etc/cni/net.d \\ # CNI configuration directory
  --cni-bin-dir=/etc/cni/bin \\ # CNI binaries directory with all the supported plugins
  --register-node=true \\
  --v=2
```

```yaml
# kubelet-config.yaml
staticPodPath: /etc/kubernetes/manifests
```

- The options can be viewed at `/etc/systemd/system/kubelet.service`
- Or see the running options `px -aux | grep kubelet`
