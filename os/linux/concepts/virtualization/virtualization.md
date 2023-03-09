# Virtualization

## Hypervisor

- Program that creates and runs `virtual machines`
- `Host machine` vs. `Guest Machine`
- Hypervisors
  - `KVM`: built into the linux kernel
  - `Hyper-V`: included in MS Windows Pro versions. Can be enabled under "Program and Features - Windows features"
  - `Parallels Desktop`: for macOS
  - `VirtualBox`: commercial program by Oracle (open source)
  - `VMware`: commercial program (proprietary)

## KVM

```shell
# Tells whether virtualization is enabled (VT-x for intel)
LC_ALL=C lscpu | grep Virtualization
```
