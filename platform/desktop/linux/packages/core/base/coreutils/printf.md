# printf

- Similar to the counterpart of in the C language

```shell
readonly sysfs_efi_vars='/sys/firmware/efi/efivars'
readonly efi_gpu='gpu-power-prefs-fa4ce28d-b62f-4c99-9cc3-6815686e30f9'

chattr -i "${sysfs_efi_vars}/${efi_gpu}" 2> /dev/null
printf "\x07\x00\x00\x00\x${1}\x00\x00\x00" > "${sysfs_efi_vars}/${efi_gpu}"
```

```shell
printf /sys/class/drm/card?-eDP-?
```

```shell
# Mathemtical expressions support only integers
x=60
y=-9
printf "%f\n" $((x/y))
```