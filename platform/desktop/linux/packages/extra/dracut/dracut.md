# dracut

- Creates a`initial ramdisk environment` (`initramfs` stage - `initramfs-linux.img`)
- Alternative to `mkinitcpio`

```shell
# Generates initramfs at "/boot/initramfs-<linux>.img"
dracut -f

# Generates initramfs at custom location
dracut --hostonly --no-hostonly-cmdline /boot/initramfs-linux.img
```

- You can either pass all the desired paramters via cmdline or create config files at `/etc/dracut.conf.d/*.conf`

```conf
# /etc/dracut.conf.d/myflags.conf

hostonly="yes"
compress="lz4"
add_drivers+=" i915 "
omit_dracutmodules+=" network iscsi "
force_drivers+=" nvidia nvidia_modeset nvidia_uvm nvidia_drm " # Early kernel module loading
```
