# NixOS installation

- Installation page <https://nixos.org/manual/nixos/stable/>

```shell
# log in as root
sudo su
```

## Wi-Fi

```shell
iwctl
[iwd] device list
[iwd] station "wlan0" get-networks
[iwd] station "wlan0" connect "ssid"

# test connection
ping "nixos.org"

# update clocks
systemctl restart systemd-timesyncd
```

## Partitions

- Partition Setup
  - `g` -> New partition table
  - `n` -> New partition
  - `/dev/sdx1` -> +0.5G
  - `/dev/sdx2` -> Rest
  - `w` -> write

```shell
# List available disks and partitions
lsblk

# List disks
fdisk -l # Optionally use cgdisk
```

## Root partition: LUKS encryption

```shell
# Format encrypted partition
cryptsetup luksFormat /dev/sdxN -v -y

cryptsetup config /dev/sdxN --label FOO_CRYPT

# Unlock partition
cryptsetup open /dev/sdxN foo
```

## Root partition: EXT4 setup

```shell
# Format partition & label it
mkfs.ext4 -L FOO /dev/mapper/foo

# Mount
mount /dev/mapper/foo /mnt
```

## EFI partition

```shell
# Format
mkfs.vfat /dev/sdx1

# Set label
dosfslabel /dev/sdx1 ESP

# Mount
mount -m /dev/sdx1 /mnt/boot
```

## Configuration

- Creates
  - `/etc/nixos/configuration.nix`
  - `/etc/nixos/hardware-configuration.nix`

```shell
nixos-generate-config --root "/mnt"
```

```nix
{ config, pkgs, ... }: {
  imports = [
    "${builtins.fetchGit { url = "https://github.com/kekrby/nixos-hardware.git"; }}/apple/t2"
  ];
  hardware.firmware = [
    (pkgs.stdenvNoCC.mkDerivation {
      name = "brcm-firmware";

      buildCommand = ''
        dir="$out/lib/firmware"
        mkdir -p "$dir"
        cp -r ${./files/firmware}/* "$dir"
      '';
    })
  ];
  programs.hyprland.enable = true;
}

```

## Install

```shell
nixos-install
reboot
```
