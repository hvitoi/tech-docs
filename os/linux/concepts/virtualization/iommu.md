# IOMMU (Input/Output Memory Management Unit)

- `Intel VT-d` or `AMD-Vi`
- Creates a virtual address so that multiple systems can access the same device
- The virtual addresses can be passed to VMs so that they can extract the most of it (e.g., gpus)

## Kernel parameters

```conf
intel_iommu=on # enable iommu for intel processors (for amd it's already on by default)
iommu=pt # do not touch the devices which cannot be passed through
```

## Groups

- An IOMMU group is the smallest set of physical devices that can be passed to a VM
- A group can be passed to a VM withouta affecting the other groups

```shell
#!/bin/bash
shopt -s nullglob
for g in $(find /sys/kernel/iommu_groups/* -maxdepth 0 -type d | sort -V); do
    echo "IOMMU Group ${g##*/}:"
    for d in $g/devices/*; do
        echo -e "\t$(lspci -nns ${d##*/})"
    done;
done;
```

## VFIO

- It's a linux module that offer stub (dummy/placeholder) drivers to be attached to devices on the host system that will be passed through to a VM
- This prevents the host machine to interact with the device
