# devtmpfs

- Mounted at `/dev`
- `Udev` is responsible for the dynamic device management needed for hot plugging devices
- Whenever a device is plugged
  - The kernel emits an event
  - Systemd (`systemd-udevd.service`) listens the event
  - The daemon creates a file in /dev
- The udev daemon searches configured rules to match the event with a rule to identify the device

## Udev Rules

- Location
  - `/usr/lib/udev/rules.d`: default rules (do not edit)
  - `/etc/udev/rules.d`: customized rules (free to edit)
- Lower-numbered rule files are processed first
  - That can prevent a rule in a higher-numbered rule to make a change by using the `:=` assignment operator

### Match conditions

- Equality operators
  - `==`: equals
  - `!=`: does not equal
- Types
  - **KERNEL**
  - **ATTRS**
  - **ENV**: by property

### Actions

- Assignment operators
  - `=` (overwrite and assign)
  - `+=` (add without overwriting, append)
  - `:=` (add and prevent other rules from overwriting)
- Types

  - **ATTR**: change attribute
  - **MODE**: change the device file permission
  - **SYMLINK**: create a symbolic link at a location (relative to /dev)
  - **TAG**
  - **ENV**: add a property

- The actions are taken only if all the match conditions are met

### Examples

```conf
# Assigns the i2c devices to group i2c, and gives that group RW access:
# Assign RW access to /dev/i2c* devices whenever the user is in i2c group
KERNEL=="i2c-[0-9]*", GROUP="i2c", MODE="0660"

# Gives everyone RW access to the /dev/i2c devices
KERNEL=="i2c-[0-9]*", MODE="0666"

# Assign a tag to the device /dev/dri/card1 whenever it's plugged
ENV{DEVNAME}=="/dev/dri/card1", TAG+="mutter-device-preferred-primary"

# Assign a tag to the gpu device that matches the vid and pid
SUBSYSTEM=="drm", KERNEL=="card*", ATTRS{idVendor}=="1002", ATTRS{idProduct}=="73ff", TAG+="mutter-device-preferred-primary"

# Assign tag by ID_PATH
SUBSYSTEM=="drm", ENV{ID_PATH}=="pci-0000:0e:00.0", TAG+="mutter-device-preferred-primary"

# If a env is define then take the run a command
ENV{SOME_ENV}=="?*" IMPORT{program}="ls -la"
```
