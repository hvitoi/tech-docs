# udevadm

## info

- Query `sysfs` or the `udev` database.
- This can be used to get properties to be used as match conditions

```shell
# by devpath
udevadm info \
  "/dev/dri/card2"

# by path syspath (relative to /sys)
udevadm info \
  --path "devices/pci0000:00/0000:00:01.1/0000:06:00.0/0000:07:01.0/0000:0a:00.0/0000:0b:01.0/0000:0c:00.0/0000:0d:00.0/0000:0e:00.0/drm/card2"

# by node or symlink name
udevadm info \
  --name "/dev/dri/card2"
```

```shell
# query
udevadm info \
  "/dev/dri/card1"
  --query "all" # default option
  # --query "name" # N (NAME). E.g., dri/card1
  # --query "symlink" # S (SYMLINK). E.g., dri/by-path/pci-0000:0e:00.0-card
  # --query "path" # P (PATH). E.g., /devices/pci0000:00/.../0000:0e:00.0>
  # --query "property" # E (ENV). E.g., ID_PATH=pci-0000:0e:00.0

# print the device information and all its parents
# all the properties can be used in udev rules to match the specified device
udevadm info \
  "/dev/dri/card1" \
  --attribute-walk
```

## control

```shell
# reload udev rules
udevadm control --reload-rules && udevadm trigger
```

```shell
udevadm control --log-priority=debug
journalctl -f
```

## trigger

```shell
# retrigger the device events
udevadm trigger
```

## monitor

- Monitor udev events

```shell
udevadm monitor
udevadm monitor --subsystem-match "drm"
```
