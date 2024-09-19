# bootctl

- `systemd-boot` (formerly gummiboot) is a EFI boot manager

## Partitions

- `<esp>` is the mount point of the ESP partition
- ESP partition is recommended be mount ESP to `/efi`
- If using a extended boot loader partition, it's recommended to be mounted at `boot`

- **Warning**: if you create a `/efi` folder, systemd will automatically mount the esp partition into it
  - If you want to remove this folder and the auto mount you need to stop the unit `efi.automount` (you can see it with `systemctl list-units --type=automount`)

## install

- Copies the systemd-boot bootloader into ESP partition
- Creates a EFI boot entry in EFI partition
- `/usr/lib/systemd/boot/efi/systemd-bootx64.efi` will be copied to:
  - `<esp>/EFI/systemd/systemd-bootx64.efi` and `<esp>/EFI/BOOT/BOOTX64.EFI`

```shell
bootctl install # Locate esp-path at "/efi", "/boot" or "/boot/efi". Locate boot-path (if any) at "/boot"
bootctl --esp-path=/a --boot-path /b install # force path
```

## Auto Probe

- systemd-boot automatically check for windows boot entry at `/EFI/Microsoft/Boot/Bootmgfw.efi`

## Configuration

```txt
<esp>/loader/
├── entries
│   ├── arch.conf
├── entries.srel
├── loader.conf
└── random-seed
```

### loader.conf

```conf
# <esp>/loader/loader.conf

# the default boot entry
default arch.conf

# time to wait the pick entries screen
timeout 2 # 2 seconds
timeout 0 # no menu is shown and a key (e.g., space) needs to be pressed to show the menu.
timeout menu-hidden # same as above
timeout menu-force # always show without a stopwatch

# resolution of the menu
console-mode 0

# Allows changing kernel parameters on the fly
editor true # enabled by default

# automatically discover boot entries (e.g., windows boot)
auto-entries true # enabled by default

# boot to firmware entry option (firmware may still be reached using "f" key)
auto-firmware true # enabled by default

# Beeped timeout
beep false # disabled by default
```

## entries.srel

- Usually `type1`

### entries

- `title`: name of the system to be boot
- `version`: version of the system (when multiple entries with the same title exist)
- `efi`: efi system to start
- `linux`: convenience for "efi path"
- `options`: parameters to be passed to the efi program (or kernel parameters)
- `initrd`: convenience for "options initrd=path"

```conf
# <esp>/loader/entries/arch.conf
title Arch Linux
linux /vmlinuz-linux
initrd /initramfs-linux.img
initrd /intel-ucode.img
options root=PARTUUID=d340b3e6-85af-4d4b-bf60-242614758599 rw # kernel parameters are defined here
```

- Get the root PARTUUID with `blkid`
