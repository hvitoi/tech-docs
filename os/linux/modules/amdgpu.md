# amdgpu

- Start this module in early KMS (Kernel mode setting) - during the `initramfs stage` - if you are having trouble on making an eGPU as primary

```conf
# /etc/mkinitcpio.conf

MODULES=(... amdgpu ...)
```
