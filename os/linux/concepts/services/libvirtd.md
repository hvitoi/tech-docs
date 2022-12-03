# libvirtd

- Daemon to interact with KVM

```shell
systemctl enable libvirtd.service
```

```shell
# add yourself into the libvirt group to be able to run vms without root
usermod -aG "libvirt" $USER
```
