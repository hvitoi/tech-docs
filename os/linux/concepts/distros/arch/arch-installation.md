# Arch installation

- Installation image: <https://archlinux.org/download/>

## Connect to Wi-Fi

```shell
# Connect to Wi-Fi
iwctl
[iwd] device list
[iwd] station "wlp3s0" get-networks
[iwd] station "wlp3s0" connect "ssid"
ping "archlinux.org" # test connection
```

## Partitions

```shell
# List available disks and partitions
lsblk

# List disks
fdisk -l # Optionally use cgdisk

# Format
mkfs.vfat "/dev/sdx1" # efi partition (use 300 MB)
mkfs.ext4 "/dev/sdx2" # root partition
```

## Encryption (optional)

```shell
# Format encrypted partition
cryptsetup luksFormat "/dev/sdx2" -v -y

# Unlock partition
cryptsetup open "/dev/sdx2" "sun"

# Format partition
mkfs.ext4 "/dev/mapper/sun"
```

## Mounting

```shell
# Mount root partition
mount "/dev/sdx2" "/mnt" # if not encrypted
mount "/dev/mapper/sun" "/mnt" # if encrypted

# Mount efi partition
mount -m "/dev/sdx1" "/mnt/boot"
```

## Swap (optional)

```shell
dd if="/dev/zero" of="/swapfile" bs="1M" count="1024" status="progress" # 1GB swap file (only for UEFI systems)
chmod 600 "/swapfile"
mkswap "/swapfile" # optionally use a swap partition /dev/sdx4
swapon "/swapfile" # or /dev/sdx4
```

## Install System

```shell
# Update mirrors
pacman -Syy

# Install system
pacstrap "/mnt" "linux" "linux-firmware" "base" "base-devel" "vim" "zsh" # add "intel-ucode" or "amd-ucode"

# Generate fstab
genfstab -U "/mnt" >> "/mnt/etc/fstab"

# Chroot
arch-chroot "/mnt"
```

## Initial ramdisk environment

- Necessary for encrypted drivers only
- Modify the file `/etc/mkinitcpio.conf` and add the hooks
  - `keyboard`
  - `encrypt`

```conf
HOOKS=(base udev autodetect keyboard modconf block encrypt filesystems fsck)
```

## Boot loader & Kernel parameters

```shell
# Install systemd-boot
bootctl install
```

```conf
# efi/loader/loader.conf
default arch.conf
timeout 2
```

```conf
# efi/loader/entries/arch.conf
title Arch Linux
linux /vmlinuz-linux
initrd /initramfs-linux.img
options root=UUID=310bac7d-c20d-4cc0-a7eb-2e5e71d7baab rw # for unencrypted devices
options cryptdevice=UUID=310bac7d-c20d-4cc0-a7eb-2e5e71d7baab:sun root=/dev/mapper/sun rw # for encrypted devices
```

- Get the root PARTUUID with `blkid`

## Packages

```shell
# Gnome DE
pacman -S "gnome" "gnome-tweaks" "gnome-themes-extra" "networkmanager" "bluez-utils"

# Sway DE
pacman -S "sway" "swaylock" "swayidle" "dmenu" "alacritty" "xdg-desktop-portal-wlr" "networkmanager" "bluez"

# Other utils
pacman -S "firefox" "solaar" "dkms" "tilix" "pipewire-pulse" "pipewire-alsa" "pavucontrol" "mesa" "mesa-utils" "steam
```

## Services

```shell
# Enable services
systemctl enable "gdm.service" # for gnome only
systemctl enable "NetworkManager.service"
systemctl enable "bluetooth.service"
```

## Configuration

```shell
# Time zone
ln -sf "/usr/share/zoneinfo/America/Sao_Paulo" "/etc/localtime"
hwclock --systohc

# Localization
vim "/etc/locale.gen" # Uncomment the desired locale
locale-gen # Generate config
echo "LANG=en_US.UTF-8" >> /etc/locale.conf
echo "KEYMAP=br-abnt2" >> /etc/vconsole.conf

# Network
echo "sun" >> /etc/hostname
echo "127.0.0.1 localhost" >> /etc/hosts
echo "::1 localhost" >> /etc/hosts

# User
useradd -m -d "/home/hvitoi" -s "/bin/zsh" "hvitoi" # new user
usermod -aG "wheel" "hvitoi" # add into a group
passwd "hvitoi" # change password
EDITOR=vim visudo # Uncomment %wheel ALL=(ALL) ALL
```

## Finish

```shell
# Exit chroot
exit

# Reboot
reboot
```
