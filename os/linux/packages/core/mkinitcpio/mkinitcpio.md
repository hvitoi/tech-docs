# mkinitcpio

- It's a bash script used to create an `initial ramdisk environment` (`initramfs` stage - `initramfs-linux.img`)
- The initial ramdisk is a very small environment (early userspace) which early loads various kernel modules and sets up necessary things before handing over control to init

```shell
# All presets
mkinitcpio -P

# Only linux-lts
mkinitcpio -p "linux-lts"
```

- Missing hardware firmware will be shown

## Preset

- Presets for each kernel is stored at `/etc/mkinitcpio.d/`
  - E.g., `/etc/mkinitcpio.d/linux.preset`

```shell
# generate presets for all kernels
mkinitcpio install
```

```conf
# mkinitcpio preset file for the 'linux' package

ALL_config="/etc/mkinitcpio.conf"
ALL_kver="/boot/vmlinuz-linux"

PRESETS=('default' 'fallback')

#default_config="/etc/mkinitcpio.conf"
default_image="/boot/initramfs-linux.img"
#default_options=""

#fallback_config="/etc/mkinitcpio.conf"
fallback_image="/boot/initramfs-linux-fallback.img"
fallback_options="-S autodetect"

```

## Configuration File

- Config file: `/etc/mkinitcpio.conf`
- The `MODULES` array is used to specify modules to load before anything else is done

```conf
MODULES=(i915)
```

- After that mkinitcpio must be run to regenerate the script
