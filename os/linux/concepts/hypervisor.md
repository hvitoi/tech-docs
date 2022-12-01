# Hypervisor

- Program that creates and runs `virtual machines`
- `Host machine` vs. `Guest Machine`
- Hypervisors
  - `KVM`: built into the linux kernel
  - `Hyper-V`: included in MS Windows Pro versions. Can be enabled under "Program and Features - Windows features"
  - `Parallels Desktop`: for macOS
  - `VirtualBox`: commercial program by Oracle (open source)
  - `VMware`: commercial program (proprietary)

## KVM

```sh
# Tells whether virtualization is enabled (VT-x for intel)
LC_ALL=C lscpu | grep Virtualization
```

- Useful packages

  - `qemu-desktop`: vm emulator (uses KVM or Zen under the hood). It's the API, command line
  - `virt-manager`: GUI for managing VMs (`libvirt` is installed as a dependency)
  - `gnome-boxes`: GUI for managing VMs (also uses `libvirt`)
  - `dnsmasq`: networking

  - `qemu-arch-extra`: allow virtualizing different architectures
  - `ovmf`: allows VM with UEFI
  - `vde2`: networking tool
  - `ebtables`: networking
  - `bridge-utils`: networking
  - `openbsd-netcat`: networking

```sh
# Starts KVM daemon
systemctl enable libvirtd.service
```
