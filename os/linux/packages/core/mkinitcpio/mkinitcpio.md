# mkinitcpio

- It's a bash script used to create an `initial ramdisk environment` (`initramfs` stage - `initramfs-linux.img`)
- Creates the initramfs/initrd (initial RAM filesystem (initramfs) / initial RAM disk (initrd))
- The initial ramdisk is a very small environment (early userspace) which early loads various kernel modules and sets up necessary things before handing over control to init

## Generate

```shell
# Generate images based on preset file configuration
mkinitcpio -P # for all presets
mkinitcpio -p "linux-lts" # specified preset
```

```shell
# Generate image based on parameter configuration
mkinitcpio \
  --config "/etc/mkinitcpio.conf" \ # defaults to /etc/mkinitcpio.conf
  --kernel "6.0.12-arch1-1" \ # defaults to the current running (installed kernels can be found at /usr/lib/modules)
  --generate "/boot/initramfs-linux.img"
```

```shell
# list all available hooks
mkinitcpio -L

# help text for a specific hook
mkinitcpio -H "base"
```

## Preset

- Every time a kernel is installed or upgraded, a pacman hook automatically generates a `.preset` file
- Presets for each kernel are stored at `/etc/mkinitcpio.d/`
- /etc/mkinitcpio.d/
- It's a list of information required to create initial ramdisk images
- The preset is used so that manually specifying the various parameters is not needed when generating the image

```shell
# manually generate presets for all kernels
mkinitcpio install
```

```conf
# /etc/mkinitcpio.d/linux.preset
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
- After that mkinitcpio must be run to regenerate the script

```conf
# modules to be added to the image
# modules suffixed with "?" will not throw error if not found
MODULES=(i915, apple_bce?)

# binaries to be added to the image (added before hooks are run)
BINARIES=()

# files to be added to the image (added before hooks are run)
FILES=()

# hooks to be run during the build process (order is important)
HOOKS=(base udev autodetect modconf kms keyboard block encrypt filesystems fsck)
```
