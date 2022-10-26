# mkinitcpio

- It's a bash script used to create an `initial ramdisk environment` (`initramfs` stage - `initramfs-linux.img`)
- The initial ramdisk is a very small environment (early userspace) which early loads various kernel modules and sets up necessary things before handing over control to init

```sh
# All presets
mkinitcpio -P

# Only linux-lts
mkinitcpio -p "linux-lts"
```

- Missing hardware firmware will be shown

## Configuration File

- Config file: `/etc/mkinitcpio.conf`
- The `MODULES` array is used to specify modules to load before anything else is done

```conf
MODULES=(i915)
```

- After that mkinitcpio must be run to regenerate the script
