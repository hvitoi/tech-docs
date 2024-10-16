# machine

- Manage a Linux Virtual Machines
- Necessary for macOS systems

- The command is sent to the VM's socket through ssh
- The `gvproxy` application manages port mapping between the host and VM

## init

- Creates a new Fedora CoreOS Linux VM
- By default uses `applehv` on MacOS (instead of `qemu`)
- The default VM name is `podman-machine-default`

```shell
podman machine init # rootless, 5 cpus, 2048 memory by default

podman machine init --rootful --cpus 2 --memory 4096
```

## list

- List all existing VMs

```shell
podman machine list
```

## info

- Config dir: `~/.config/containers/podman/machine/applehv`
- Image dir: `~/.local/share/containers/podman/machine/applehv`

```shell
# display config about the created VMs
podman machine info
```

## inspect

```shell
# all VMs
podman machine inspect

# specific VM
podman machine inspect podman-machine-default
```

## start

- Start an existing VM

```shell
podman machine start
```

## ssh

- ssh into the vm in a bash shell

```shell
podman machine ssh <vm>
```

## set

```shell
# Rootless by default, this allows root access to the vm
podman machine set --rootful
podman machine set --usb vendor=0781,product=5590 # usb passthrough
podman machine ssh dmesg | grep -i "0781\|5590" # verify that the usb has been passed through
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
