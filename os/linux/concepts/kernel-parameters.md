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
