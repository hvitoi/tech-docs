# udevadm

## info

- Query sysfs or the udev database.
- This can be used to get properties to be used as match conditions

```shell
# print the device information for usage in udev rules
udevadm info "/dev/dri/card1" \
  --query "all"
  # --query "name" # N (NAME). E.g., dri/card1
  # --query "symlink" # S (SYMLINK). E.g., dri/by-path/pci-0000:0e:00.0-card
  # --query "path" # P (PATH). E.g., /devices/pci0000:00/.../0000:0e:00.0>
  # --query "property" # E (ENV). E.g., ID_PATH=pci-0000:0e:00.0

# by node name
udevadm info
  --name "/dev/dri/card1"

# print the device information and all its parents
# all the properties can be used in udev rules to match the specified device
udevadm info "/dev/dri/card1" \
  --query "all" \
  --attribute-walk
```

## controlq

```shell
# reload udev rules
udevadm control --reload-rules && udevadm trigger
```

## trigger

```shell
# retrigger the device events
udevadm trigger
```
