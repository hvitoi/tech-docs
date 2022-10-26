# mac-firmware

## gpu-switch

- This sets the `gpu-power-prefs` NVRAM variable to make the iGPU/dGPU/eGPU the Boot GPU

```sh
# use integrated gpu as primary on next boot
gpu-switch -i

# use dedicated gpu as primary on next boot
gpu-switch -d
```
