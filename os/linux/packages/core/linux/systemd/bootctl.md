# bootctl

- The `esp` mountpoint is usually `/efi` or `/boot` (preferred)

## install

- Copies the systemd-boot bootloader into ESP partition (mounted at /boot)
- Creates a EFI boot entry in EFI partition
- `/usr/lib/systemd/boot/efi/systemd-bootx64.efi` will be copied to:
  - `esp/EFI/systemd/systemd-bootx64.efi` and `esp/EFI/BOOT/BOOTX64.EFI`

```shell
bootctl install # Locate esp-path at "/efi", "/boot" or "/boot/efi". Locate boot-path (if any) at "/boot"
bootctl --esp-path=/a --boot-path /b install # force path
```

## Partitions

- ESP partition is recommended be mount ESP to `/efi`
- If using a extended boot loader partition, it's recommended to be mounted at `boot`

- **Warning**: if you create a `/efi` folder, systemd will automatically mount the esp partition into it
  - If you want to remove this folder and the auto mount you need to stop the unit `efi.automount` (you can see it with `systemctl list-units --type=automount`)

## Configuration

```conf
# esp/loader/loader.conf
timeout 2
default arch
```

```conf
# esp/entries/arch.conf
title Arch Linux
linux /vmlinuz-linux
initrd /intel-ucode.img
initrd /initramfs-linux.img
options root=PARTUUID=d340b3e6-85af-4d4b-bf60-242614758599 rw
```

- Get the root PARTUUID with `blkid`
