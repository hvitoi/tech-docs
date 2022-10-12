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
pci=hpbussize=0x33,hpmemsize=4M,hpmmiosize=128M,realloc
pci=hpbussize=0x10,hpmmiosize=32M,hpmmioprefsize=512M,realloc,assign-busses,nocrs
```

## iommu

```conf
iommu=on
iommu=pt
```

## iommu.passthrough

```conf
iommu.passthrough=1
```

## intel_iommu

```conf
intel_iommu=on
```

## nowatchdog

- Disable watchdog timers. It's not necessary for personal laptops

```conf
nowatchdog
```
