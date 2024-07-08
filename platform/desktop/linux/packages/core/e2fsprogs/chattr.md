# chattr

- Change attribute of a mounted filesystem
- Low-level alternative to file permissions

```shell
readonly sysfs_efi_vars='/sys/firmware/efi/efivars' # mountpoint of efivars
readonly efi_gpu='gpu-power-prefs-fa4ce28d-b62f-4c99-9cc3-6815686e30f9'

# Ensure efi vars are mounted
mount -l | grep efivars

# Remove immutable bit, allows modification
chattr -i "${sysfs_efi_vars}/${efi_gpu}" 2> /dev/null

# Set NVRAM
printf "\x07\x00\x00\x00\x1\x00\x00\x00" > "${sysfs_efi_vars}/${efi_gpu}"
```

```shell
# protect against accidental file deletion the immutable flag
sudo chattr +i /critical/directory/or/file
```
