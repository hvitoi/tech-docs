# bootctl

- The `esp` mountpoint is usually `/efi` or `/boot` (preferred)

## install

- Copies the systemd-boot bootloader into ESP partition (mounted at /boot)
- Creates a EFI boot entry in EFI partition
- `/usr/lib/systemd/boot/efi/systemd-bootx64.efi` will be copied to:
  - `esp/EFI/systemd/systemd-bootx64.efi` and `esp/EFI/BOOT/BOOTX64.EFI`

```sh
bootctl install # Locate esp-path at "/efi", "/boot" or "/boot/efi". Locate boot-path (if any) at "/boot"
bootctl --esp-path=/a --boot-path /b install # force path
```

## Partitions

- ESP partition is recommended be mount ESP to `/efi`
- If using a extended boot loader partition, it's recommended to be mounted at `boot`

- **Warning**: if you create a `/efi` folder, systemd will automatically mount the esp partition into it
  - If you want to remove this folder and the auto mount you need to stop the unit `efi.automount` (you can see it with `systemctl list-units --type=automount`)

## Configuration

### loader

- `default`: the default boot entry
- `timeout`: seconds to wait the pick entries screen

```conf
# esp/loader/loader.conf
default arch.conf # name of the system
timeout 2 # if "0" or "menu-hidden", no menu is shown and a key (e.g., space) needs to be pressed to show the menu. if "menu-force" the menu is always shown without a stopwatch
console-mode 0 # resolution of the menu
editor true # enable (default) the modification of kernel parameters on the fly
auto-entries true # enable (default) the automatically discovered boots (e.g., windows boot)
auto-firmware true # enable (default) the boot to firmware entry option (firmware may still be reached using "f" key)
beep false # beeped timeout, disabled by default
```

### entries

- `title`: name of the system to be boot
- `version`: version of the system (when multiple entries with the same title exist)
- `efi`: efi system to start
- `linux`: convenience for "efi path"
- `options`: parameters to be passed to the efi program (or kernel parameters)
- `initrd`: convenience for "options initrd=path"

```conf
# esp/loader/entries/arch.conf
title Arch Linux
linux /vmlinuz-linux
initrd /intel-ucode.img
initrd /initramfs-linux.img
options root=PARTUUID=d340b3e6-85af-4d4b-bf60-242614758599 rw # kernel parameters are defined here
```

- Get the root PARTUUID with `blkid`

## Other systems

- systemd-boot automatically check for windows boot entry at `/EFI/Microsoft/Boot/Bootmgfw.efi`
