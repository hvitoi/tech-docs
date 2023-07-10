# sysfs

- Mounted at `/sys`
- It's a filesystem that allows `kernel subsystems` to report kernel objects, object attributes, and object relationships to user space
- It's always mounted to `/sys` at the system startup (before fstab is read)

```shell
mount | grep sysfs
```

## devices

- Every hardware attached to the computer
  - E.g., `/sys/devices/pci0000:00/0000:00:00.0`

## block

- Devices that are storage
- Usually link files that point to `devices`

## bus

- `/sys/bus/pci/devices/`: all pci devices

  - Actually points to `/sys/devices/pci0000:00/`

- GPU
  - `/sys/bus/pci/devices/0000:03:00.0`
  - `/sys/bus/pci/devices/0000:03:00.0/boot_vga`: whether the GPU will be used for booting (1 or 0)
  - `/sys/bus/pci/devices/0000:03:00.0/current_link_speed`: PCI speed
  - `/sys/bus/pci/devices/0000:03:00.0/driver`: example: amdgpu

```shell
set -u
for boot_vga in /sys/bus/pci/devices/*/boot_vga; do
  echo "Found vga device: ${boot_vga}"
  if [ $(<"${boot_vga}") -eq 0 ]; then
    echo "Found Boot VGA Device - false: ${boot_vga}"

    dir=$(dirname -- "${boot_vga}")
    for dev in "${dir::-1}"*; do
      echo "Devices: ${dev}"
      # echo 'vfio-pci' > "${dev}/driver_override"
    done
  else
    echo "Found Boot VGA Device - true: ${boot_vga}"
  fi
done

for f in /sys/bus/pci/devices/*/boot_vga ; do echo -n "$f:" ; cat $f ; done
```

## class

- Backlight
  - `/sys/class/backlight/gmux_backlight/brightness`
- Leds
  - `/sys/class/leds/:white:kbd_backlight/brightness`
- DRM
  - `/sys/class/drm/card2-DP-8/enabled`

```python
#!/bin/python
import subprocess
import json
import sys


def backlight_devices():
    devices_output = subprocess.check_output(
        "brightnessctl -l -m -c backlight",
        shell=True,
        encoding='utf-8',
    )

    backlight_devices = []

    for device in devices_output.splitlines():
        device_id = device.split(",")[0]

        # device_name = subprocess.check_output(
        #     "cat /sys/class/backlight/" + device_id +
        #     "/device/idModel" + "|| echo " + device_id,
        #     shell=True,
        #     encoding='utf-8',
        # ).strip()

        device_brightness_percentage = device.split(",")[3].replace("%", "")

        backlight_devices.append(
            {
                "id": device_id,
                # "name": device_name,
                "brightness_percentage": device_brightness_percentage
            })

    return backlight_devices
sys.stdout.write(json.dumps(backlight_devices()))
```
