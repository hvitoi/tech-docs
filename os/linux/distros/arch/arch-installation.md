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

## Encryption: LUKS

```shell
# Format encrypted partition
cryptsetup luksFormat "/dev/sdxN" -v -y

cryptsetup config "/dev/sdxN" --label FOO_CRYPT

# Unlock partition
cryptsetup open "/dev/sdxN" "foo"
```

## Root partition: BTRFS setup

```shell
# Format partition
mkfs.btrfs "/dev/mapper/foo"

# set filesystem label
btrfs filesystem label /dev/mapper/foo FOO

# Temporarily mount root subvolume to create the child subvolumes
mount "/dev/mapper/foo" "/mnt"

# create subvolumes
btrfs subvolume create "/mnt/@"
btrfs subvolume create "/mnt/@home"

# umount root subvolume
umount "/mnt"

# mount subvolumes
mount "/dev/mapper/foo" "/mnt" -o "compress=zstd,subvol=@"
mount -m "/dev/mapper/foo" "/mnt/home" -o "compress=zstd,subvol=@home"
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
# Setup pacman keys
pacman-key --init
pacman-key --populate
pacman-key --refresh-keys
pacman -Syy

# Install system
pacstrap -K "/mnt" "base" "base-devel" "linux" "linux-firmware" "intel-ucode"

# Generate fstab
genfstab -U "/mnt" >> "/mnt/etc/fstab"

# Chroot
arch-chroot "/mnt"
```

## Packages

```shell
# Pacman config
vim "/etc/pacman.conf" #  ParallelDownloads = 10

# Packages
pacman -S "gnome" "xdg-desktop-portal-gnome" "vim" "zsh" "networkmanager" "bluez"
```

## Initial ramdisk environment (initramfs)

- Modify the file `/etc/mkinitcpio.conf` and add the `encrypt` hooks

```conf
HOOKS=(base udev autodetect modconf kms keyboard keymap consolefont block encrypt filesystems fsck)
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
initrd /intel-ucode.img
options root=LABEL=FOO rw # for unencrypted devices
options cryptdevice=LABEL=FOO_CRYPT:sun root=/dev/mapper/sun rootflags=subvol=@ rw # for encrypted devices
```

- Get the root partition UUID with `:r !blkid` inside of vim

## Services

```shell
# Enable services
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
localectl set-locale "LANG=en_US.UTF-8"

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
