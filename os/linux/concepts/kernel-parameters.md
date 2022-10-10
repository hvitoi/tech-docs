# Kernel parameters

- <https://www.kernel.org/doc/html/v4.10/admin-guide/kernel-parameters.html>

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

## other

```conf
BOOT_IMAGE=/@/boot/vmlinuz-linux-t2
rootflags=subvol=@
fsck.mode=skip nowatchdog
nmi_watchdog=0
apparmor=1
lsm=lockdown,yama,apparmor,bpf
i915.enable_guc=2
loglevel=7
rd.udev.log_priority=3
intel_pstate=disable
```
