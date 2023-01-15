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

# partition
# +0.5G for /dev/sdx1 and the rest for /dev/sdx2
```

## Encryption

```shell
# Format encrypted partition
cryptsetup luksFormat "/dev/sdx2" -v -y

# Unlock partition
cryptsetup open "/dev/sdx2" "sun"
```

## Root partition: BTRFS setup

```shell
# Format partition
mkfs.btrfs "/dev/mapper/sun"

# Temporarily mount root subvolume to create the child subvolumes
mount "/dev/mapper/sun" "/mnt"

# create subvolumes
btrfs subvolume create "/mnt/@"
btrfs subvolume create "/mnt/@home"

# umount root subvolume
umount "/mnt"

# mount subvolumes
mount "/dev/mapper/sun" "/mnt" -o "compress=zstd,subvol=@"
mount -m "/dev/mapper/sun" "/mnt/home" -o "compress=zstd,subvol=@home"
```

## EFI partition

```shell
# Format
mkfs.vfat "/dev/sdx1"

# Mount
mount -m "/dev/sdx1" "/mnt/boot"
```

## Swap (optional)

```shell
# 1GB swap file (only for UEFI systems)
dd if="/dev/zero" of="/swapfile" bs="1M" count="1024" status="progress"

# swap file permission
chmod 600 "/swapfile"

# create swap from file
mkswap "/swapfile"

# activate swap
swapon "/swapfile" # if using a partition use its device e.g., /dev/sdy
```

## Install System

```shell
# Optionally use reflector to get the current best mirrors
reflector -l "10" --sort "rate" --save "/etc/pacman.d/mirrorlist"

# Install system
pacstrap -K "/mnt" "base" "linux" "linux-firmware"

# Generate fstab
genfstab -U "/mnt" >> "/mnt/etc/fstab"

# Chroot
arch-chroot "/mnt"
```

## Packages

```shell
# Packages
pacman -S "vim" "reflector"

# Pacman config
vim "/etc/pacman.conf" #  ParallelDownloads = 10

# Mirror list
reflector -l "10" --sort "rate" --save "/etc/pacman.d/mirrorlist"

# Update package database
pacman -Syy

# Gnome DE
pacman -S "gnome" "gnome-tweaks" "gnome-themes-extra" "networkmanager" "bluez" "bluez-utils"

# Sway DE
pacman -S "sway" "swaylock" "swayidle" "dmenu" "alacritty" "xdg-desktop-portal-wlr" "networkmanager" "bluez"

# Other packages
pacman -S "base-devel" "zsh" "firefox" "neofetch" # "intel-ucode" or "amd-ucode"
```

## Initial ramdisk environment (initramfs)

- Necessary for encrypted drivers only
- Modify the file `/etc/mkinitcpio.conf` and add the hooks
  - `keyboard`
  - `encrypt`

```conf
HOOKS=(base udev autodetect modconf kms keyboard block encrypt filesystems fsck)
BINARIES=(btrfs) # if btrfs root partition
```

```shell
mkinitcpio -P
```

## Boot loader & Kernel parameters

```shell
# Install systemd-boot
bootctl install
```

```conf
# efi/loader/loader.conf
default arch.conf
timeout menu-hidden
```

```conf
# efi/loader/entries/arch.conf
title Arch Linux
linux /vmlinuz-linux
initrd /initramfs-linux.img
options root=UUID=310bac7d-c20d-4cc0-a7eb-2e5e71d7baab rw # for unencrypted devices
options cryptdevice=UUID=310bac7d-c20d-4cc0-a7eb-2e5e71d7baab:sun root=/dev/mapper/sun rootflags=subvol=@ rw # for encrypted devices
```

- Get the root partition UUID with `:r !blkid` inside of vim

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
vim "/etc/locale.gen" # Uncomment the desired locale (de_DE.utf8, en_US.utf8, pt_BR.utf8)
locale-gen # Generate config
echo "LANG=en_US.UTF-8" >> /etc/locale.conf # or localectl set-locale "LANG=en_US.UTF-8"
echo "KEYMAP=br-abnt2" >> /etc/vconsole.conf

# Network
echo "lol" >> /etc/hostname
echo "127.0.0.1 localhost" >> /etc/hosts
echo "::1 localhost" >> /etc/hosts

# User
useradd -m -d "/home/me" -s "/bin/zsh" "me" # new user
usermod -aG "wheel" "me" # add into a group
passwd "me" # change password
EDITOR=vim visudo # Uncomment %wheel ALL=(ALL) ALL
```

## Finish

```shell
# Exit chroot
exit

# Reboot
reboot
```
