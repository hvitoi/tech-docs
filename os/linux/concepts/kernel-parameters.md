# Kernel parameters

- <https://www.kernel.org/doc/html/v4.10/admin-guide/kernel-parameters.html>

## root

- What device to be used as root partition while booting

```conf
root=/dev/mapper/root
```

## rootflags

- This parameter sets the mount option string for the root filesystem (same as in fstab)

```conf
# BTRFS setup
rootflags=subvol=@
```

## rw/ro

- Mount the root fs as read-write or read-only
- `rw` is the default

```conf
rw
ro
```

## BOOT_IMAGE

```conf
BOOT_IMAGE=/@/boot/vmlinuz-linux
```

## pcie_ports

```conf
pcie_ports=native # full PCIe capabilities
pcie_ports=compat # limited PCIe capabilities
pcie_ports=auto # capabilities depending on the bios
```

## pci

```conf
pci=
  realloc,
  nocrs,
  assign-busses,
  hpbussize=0x33,
  hpmemsize=4M,
  hpmmiosize=256M,
  hpmmioprefsize=512M
```

## intel_iommu

```conf
intel_iommu=on
```

## iommu

- Device passthrough

```conf
iommu=on
iommu=pt # pass through only devices that are supported
```

## iommu.passthrough

```conf
iommu.passthrough=1
```

## nowatchdog

- Disable watchdog timers. It's not necessary for personal laptops

```conf
nowatchdog
```
