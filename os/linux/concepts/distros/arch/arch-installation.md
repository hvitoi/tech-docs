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
mkfs.ext4 "/dev/sdx3" # home partition

# Swap
dd if="/dev/zero" of="/swapfile" bs="1M" count="1024" status="progress" # 1GB swap file (only for UEFI systems)
chmod 600 "/swapfile"
mkswap "/swapfile" # optionally use a swap partition /dev/sdx4
swapon "/swapfile" # or /dev/sdx4

# Mount partitions
mount "/dev/sdx2" "/mnt" # root
mount "/dev/sdx1" "/mnt/boot" # root
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

## Boot loader

- **systemd-boot** (recommended)

```shell
bootctl install
```

- **grub** (legacy)

```shell
# Install grub
pacman -S "grub" "efibootmgr" "os-prober" # Boot
grub-install --target="x86_64-efi" --efi-directory="/boot" --bootloader-id="GRUB"

# Generate config
# add "GRUB_DISABLE_OS_PROBER=false" to /etc/default/grub in order to detect other OSs
grub-mkconfig -o "/boot/grub/grub.cfg"
```

## Packages

```shell
pacman -S "gnome" "gnome-tweaks" "networkmanager" # for gnome
pacman -S "sway" "swaylock" "swayidle" "dmenu" "alacritty" "xdg-desktop-portal-wlr" "networkmanager" "bluez" # for sway
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

# Unmount everything
umount -a

# Reboot
reboot
```
