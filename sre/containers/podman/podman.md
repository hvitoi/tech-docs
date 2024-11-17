# Podman

```shell
podman container run docker.io/docker/whalesay
```

## Multi-arch support

Running container images built for a different CPU architecture

```shell
podman container run -it --arch=amd64 docker.io/archlinux
```
