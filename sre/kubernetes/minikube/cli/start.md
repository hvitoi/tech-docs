# start

- Start a new cluster
- Exposes apiserver on port 8443

```shell
minikube start

```

## memory

```shell
minikube start --memory "4096" # megabytes by default
minikube start --memory "4096m"
minikube start --memory "4g"
```

## driver

- If not specified, auto detects

```shell
# qemu
minikube start --driver qemu2

# docker
minikube start --driver docker

# ssh
minikube start --driver ssh

# podman (rootful)
podman machine init --rootful
minikube start --driver podman --container-runtime cri-o

# podman (rootless)
podman machine init
```

- Qemu driver: <https://minikube.sigs.k8s.io/docs/drivers/qemu/>

## network

```shell
# builtin network
minikube start --driver qemu --network builtin
```
