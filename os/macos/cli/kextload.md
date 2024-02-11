# kextload

- Load kernel extensions/modules (kexts) into the kernel
- Kexts run in kernel space
- In order to load 3rd party kernel extensions, `System Extensions` must be enabled under `Privacy & security` settings

```shell
# Reference to .kext file must be the full path
kextload /Library/Extensions/zfs.kext
```
