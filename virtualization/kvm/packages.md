# Virtualization packages

## libvirt

```shell
# Starts KVM daemon
systemctl enable libvirtd.service
```

## QEMU

- `qemu-desktop`: vm emulator (uses KVM or Zen under the hood). It's the API, command line
- `qemu-arch-extra`: allow virtualizing different architectures

## Others

- `edk2-ovmf`: installed as dependency - UEFI support
- `dnsmasq`: networking

## GUI

- `virt-manager`: GUI for managing VMs
- `gnome-boxes`: GUI for managing VMs
- `swtpm`: TPM support
