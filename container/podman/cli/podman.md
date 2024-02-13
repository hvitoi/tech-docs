# podman

## info

```shell
# Info
podman info
```

## system

```shell
# Show connections with remote API (or VMs)
podman system connection list
```

## machine

- Manage a linux virtual machine
- Necessary for macOS systems

```shell
# new Fedora CoreOS Linux VM
podman machine init

# Start existing VM
podman machine start

# List
podman machine list

# Inspect all machines
podman machine inspect

# Rootless by default, this allows root access to the vm
podman machine set --rootful
podman machine set --usb vendor=0781,product=5590 # usb passthrough
podman machine ssh dmesg | grep -i "0781\|5590" # verify that the usb has been passed through

# ssh into the vm in a bash shell
podman machine ssh <vm>

# Stop existing VM
podman machine stop

# Remove
podman machine rm <vm>
```

- The VM listens on the socket `~/.local/share/containers/podman/machine/qemu/podman.sock`
- The command is sent to the VM's socket through ssh
- The `gvproxy` application manages port mapping between the host and VM
