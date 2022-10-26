# modprobe

- Load kernel module
- Loading kernel modules manually (through `modprobe`) means you will have to modprobe every time you reboot
- Modprobe by default loads modules located at the following directories (usually `.ko` extension)
  - `/lib/modules/$(uname -r)`
  - `/usr/lib/modules/$(uname -r)`

```sh
find "/lib/modules/$(uname -r)" -type "f" -name "*.ko*"
find "/usr/lib/modules/$(uname -r)" -type "f" -name "*.ko*"
```

```sh
# Activate module
modprobe "module-name"
modprobe "bonding" # And module for network bonding
modprobe "v4l2loopback" exclusive_caps=1 max_buffers=2 # virtual video devices

# Remove module
modprobe -r "module"

# Display configuration of the modules
modprobe -c
modprobe -c | grep "module-name"
```

## Automatic module loading with systemd

- To load modules upon start, modules must be defined in:
  - `/etc/modules-load.d/module-name.conf` (preferred)
  - `/usr/lib/modules-load.d/module-name.conf` (ok)
  - `/etc/modules` (deprecated)

```conf
# e.g. /etc/modules-load.d/v4l2loopback.conf
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.
v4l2loopback
```

### Module default configuration

- Default configuration for the modules is stored at either
  - `/etc/modprobe.d`
  - `/usr/lib/modprobe.d`

```conf
# e.g., /etc/modprobe.d/v4l2loopback.conf
options v4l2loopback exclusive_caps=1
```

### udev

- Udev rules folder

```sh
sudo cp "/usr/share/ddcutil/data/45-ddcutils-i2c.rules" "/etc/udev/rules.d" # Copy the udev rule for the new group to rules.d
```
