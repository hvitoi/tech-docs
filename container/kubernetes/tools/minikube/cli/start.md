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
minikube start --driver "qemu2"
minikube start --driver "docker"
minikube start --driver "podman"
minikube start --driver "ssh"
```

- Qemu driver: <https://minikube.sigs.k8s.io/docs/drivers/qemu/>

## network

```shell
# builtin network
minikube start --driver qemu --network builtin
```
