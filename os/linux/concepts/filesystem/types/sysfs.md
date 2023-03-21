# sysfs

- Mounted at `/sys`
- It's a filesystem that allows `kernel subsystems` to report kernel objects, object attributes, and object relationships to user space
- It's always mounted to `/sys` at the system startup (before fstab is read)

```shell
mount | grep sysfs
```

## block

- Devices that are storage
- Usually link files that point to `devices`

## devices

- Every hardware attached to the computer
  - E.g., `/sys/devices/pci0000:00/0000:00:00.0`

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
```
