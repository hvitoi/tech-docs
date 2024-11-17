# Container

- Container reuses the `same kernel as the host` but running in an isolated environment
- Container is not a new term, it does already exist in linux as `namespaces` and `chroot`
- The host kernel uses `cgroups` and `capabilities` to limit the resources and capabilities available to the processes running in the container
- It's hidden from the container
  - The processes (/proc)
  - The filesystem on the "host" (/)
  - Network (points to a new virtual network)
  - Mounts (/dev & /sys)
  - ...
- `Open Container Initiative`: creates open industry standards around container formats and runtimes (created in 2015 by Docker)

## Container vs. VM

- **Process visibility**
  - _Container_: processes run inside of the container will also appear on the host mixed together
  - _VM_: processes processes run inside of the container will not appear on the host

- **Virtualization**
  - _Container_: does not make use of `virtualization`. There is `no hypervisor`. Because it reuses the same kernel of the host
  - _VM_: uses virtualization to boot a new kernel

## Container runtime

### runc

- Used by Kubernetes and Podman
- The `config.json` file specifies how the container will be run based on an image
- Runs in userland (`rootless`) `without a daemon`
- It's simpler and lighter than containerd

```shell
# Creates a sample OCI config file
runc spec

# Create a OCI (based on the config file) and run it
runc run <image-name>
```

### containerd

- Used by Docker
- Runs as a daemon with root permissions

## Capabilities

- Set which capabilities will be available to the processes running in the container
- Get the capability codes with `capsh --decode=<hex>` or with `man capabilities`
