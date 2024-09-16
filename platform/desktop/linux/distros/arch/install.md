# Arch installation

- Installation image: <https://archlinux.org/download/>

## Wi-Fi

```shell
iwctl
[iwd] device list
[iwd] station "wlp3s0" get-networks
[iwd] station "wlp3s0" connect "ssid"
ping "archlinux.org" # test connection
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

## Root partition: BTRFS setup

```shell
# Format partition
mkfs.btrfs /dev/mapper/foo

# set filesystem label
btrfs filesystem label /dev/mapper/foo FOO

# Temporarily mount root subvolume to create the child subvolumes
mount /dev/mapper/foo /mnt

# create subvolumes
btrfs subvolume create /mnt/@
btrfs subvolume create /mnt/@home

# umount root subvolume
umount /mnt

# mount subvolumes
mount /dev/mapper/foo /mnt -o subvol=@
mount -m /dev/mapper/foo /mnt/home -o subvol=@home
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

## Swap (optional)

```shell
# 1GB swap file (only for UEFI systems)
dd \
  if=/dev/zero \
  of=/swapfile \
  bs=1M \
  count=1024 \
  status=progress

# swap file permission
chmod 600 /swapfile

# create swap from file
mkswap /swapfile

# activate swap
swapon /swapfile # if using a partition use its device e.g., /dev/sdy
```

## Install System

```shell
# Setup pacman keys
pacman-key --init
pacman-key --populate
pacman-key --refresh-keys
pacman -Syy
```

```shell
# Install system
pacstrap /mnt base base-devel linux linux-firmware intel-ucode vim

# Generate fstab
genfstab -L /mnt >> /mnt/etc/fstab

# Chroot
arch-chroot /mnt
```

## Boot loader & Initial Ramdisk Environment

```shell
# Install systemd-boot
bootctl install
```

```conf
# /boot/loader/loader.conf
default arch.conf
timeout menu-hidden
```

```conf
# /boot/loader/entries/arch.conf
title Arch Linux
linux /vmlinuz-linux
initrd /initramfs-linux.img
initrd /intel-ucode.img
options root=LABEL=FOO rootflags=subvol=@ loglevel=3
```

```conf
# /etc/mkinitcpio.conf
MODULES=()
BINARIES=()
FILES=()
HOOKS=(base systemd autodetect modconf block filesystems keyboard sd-encrypt)
```

```conf
# /etc/crypttab.initramfs
sun LABEL=FOO_CRYPT
```

```shell
mkinitcpio -P
```

## Packages

```shell
# Pacman config
vim /etc/pacman.conf #  ParallelDownloads = 10

# Packages
pacman -S gnome networkmanager
```

```shell
# Enable services
systemctl enable NetworkManager.service
systemctl enable bluetooth.service
systemctl enable gdm.service
```

## Configuration

```shell
# Time zone
ln -sf \
  /usr/share/zoneinfo/America/Sao_Paulo \
  /etc/localtime
hwclock --systohc

# Localization
vim /etc/locale.gen # Uncomment the desired locale (de_DE.utf8, en_US.utf8, pt_BR.utf8)
locale-gen # Generate config
echo "LANG=en_US.UTF-8" >> /etc/locale.conf

# Network
echo "lol" >> /etc/hostname
echo "127.0.0.1 localhost" >> /etc/hosts
echo "::1 localhost" >> /etc/hosts

# User
useradd -m -d /home/me -s /bin/bash me # new user
usermod -aG wheel me # add into a group
passwd me # change password
EDITOR=vim visudo # Uncomment %wheel ALL=(ALL) ALL
```

## Finish

```shell
# Exit chroot
exit

# Reboot
reboot
```
