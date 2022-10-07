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
pci=hpbussize=0x33,hpmemsize=4M,hpmmiosize=128M,realloc,assign-busses,nocrs
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
root=UUID=97455e14-2a64-4f07-a681-d75713d2a6b1
cryptdevice=UUID=d3a34309-66e3-4d6a-adc4-0711ed632717:root
rw
rootflags=subvol=@
root=/dev/mapper/root
fsck.mode=skip nowatchdog
nmi_watchdog=0
apparmor=1
lsm=lockdown,yama,apparmor,bpf
i915.enable_guc=2
loglevel=7
rd.udev.log_priority=3
intel_pstate=disable
```
