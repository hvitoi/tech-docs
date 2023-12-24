# Virtualization

- Virtualization
  - Run only the native CPU architecture
  - Faster
- Emulation
  - Run other CPU architectures
  - Slower

## Hypervisor

- Program that creates and runs `virtual machines`
- `Host machine` vs. `Guest Machine`
- Native Hypervisors
  - `KVM`: built into the linux kernel
  - `Hyper-V`: included in MS Windows Pro versions. Can be enabled under "Program and Features - Windows features"
  - `HVF`: Apple's Hypervisor framework

## VM hosts

### UTM

- For MacOS and iOS
- Based off of `QEMU`

### Parallels Desktop

- For MacOS

### VirtualBox

- Multi-platform
- Commercial program by Oracle
- Open source and free for personal use

### VMware

- Multi-platform
- Commercial program (proprietary)

## KVM

```shell
# Tells whether virtualization is enabled (VT-x for intel)
LC_ALL=C lscpu | grep Virtualization
```
