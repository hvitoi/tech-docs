# libvirtd

- Daemon to interact with KVM

```sh
systemctl enable libvirtd.service
```

```sh
# add yourself into the libvirt group to be able to run vms without root
usermod -aG "libvirt" $USER
```
