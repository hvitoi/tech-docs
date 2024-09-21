# machine

- Manage a Linux Virtual Machines
- Necessary for macOS systems

- The VM listens on the socket `~/.local/share/containers/podman/machine/qemu/podman.sock`
- The command is sent to the VM's socket through ssh
- The `gvproxy` application manages port mapping between the host and VM

## init

- Create a new Fedora CoreOS Linux VM

```shell
podman machine init # rootless, 5 cpus, 2048 memory by default

podman machine init --rootful --cpus 2 --memory 4096
```

## start

- Start an existing VM

```shell
podman machine start
```

## list

- List all existing VMs

```shell
podman machine list
```

## inspect

- Inspect all machines

```shell
podman machine inspect
```

## set

```shell
# Rootless by default, this allows root access to the vm
podman machine set --rootful
podman machine set --usb vendor=0781,product=5590 # usb passthrough
podman machine ssh dmesg | grep -i "0781\|5590" # verify that the usb has been passed through
```

## ssh

- ssh into the vm in a bash shell

```shell
podman machine ssh <vm>
```

## stop

- Stop existing VM

```shell
podman machine stop
```

## rm

```shell
podman machine rm <vm>
```

## Multi-arch support

Running container images built for a different CPU architecture

```shell
podman container run -it --arch=amd64 docker.io/archlinux
```
