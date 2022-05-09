# Arch installation

- Installation image: <https://archlinux.org/download/>

## Optional configuration

- Font

```shell
# Change the terminal font to 32 points
setfont ter-132n
```

- Keyboard

```shell
# List all options for keyboard keymaps
localectl list-keymaps

# Load a specific keyboard keymap
loadkeys "br-abnt2"
```

- Date

```shell
# Update system clock
timedatectl set-ntp true
```

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
# Partitions
lsblk
fdisk -l # Optionally use cgdisk
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
mkdir "/mmt/{boot,home}" # create dirs inside the sdx2 filesystem
mount "/dev/sdx1" "/mnt/boot" # boot/efi
mount "/dev/sdx3" "/mnt/home" # home
df -h # Show mounted partitions
```

## Install and initialize Core system

```shell
# Update mirrors
pacman -Syy

# Install system
pacstrap "/mnt" "linux" "linux-firmware" "base" "base-devel" # add "intel-ucode" or "amd-ucode"

# Generate fstab
genfstab -U "/mnt" >> "/mnt/etc/fstab" # by UUID
genfstab -L "/mnt" >> "/mnt/etc/fstab" # by label

# Chroot
arch-chroot "/mnt"
```

## fstab

- `fstab` file can be used to define how disk partitions, various other block devices, or remote filesystems should be mounted into the filesystem
- These definitions will be converted into `systemd mount` units dynamically at boot

```conf
# <device>                                      <dir>                   <type>  <options>               <dump>  <fsck>

# /dev/sdb3 - arch
UUID=2740a3e6-85af-4d4a-bf60-242614758599       /                       ext4    rw,relatime             0       1

# /dev/sdc - swap
UUID=be520a04-5f31-46cb-a881-29a86a1133fe       none                    swap    defaults                0       0

# /dev/sda1 - moon
#UUID=4093109d-4077-422e-a87b-fb837e63de6f      /media/hvitoi/moon      ext4    defaults,noauto         0       2
```

## General configuration

```shell
# Region
ln -sf "/usr/share/zoneinfo/America/Sao_Paulo" "/etc/localtime"
hwclock --systohc

# Locale
vi "/etc/locale.gen" # Uncomment the desired locale
locale-gen # Generate config
echo "LANG=en_US.UTF-8" >> /etc/locale.conf

# Vconsole
echo "KEYMAP=br-abnt2" >> /etc/vconsole.conf

# Hostname and hosts
echo "yourhostname" >> /etc/hostname
echo "127.0.0.1 localhost" >> /etc/hosts
echo "::1 localhost" >> /etc/hosts

# User configuration
passwd # change root password
useradd -m -d "/home/hvitoi" -s "/bin/zsh" "hvitoi" # create user
usermod -aG "wheel" "hvitoi" # add user to a group
passwd "hvitoi" # change user password
EDITOR=vim visudo # Uncomment %wheel ALL=(ALL) ALL
```

## Additional packages

```shell
pacman -S "grub" "efibootmgr" "os-prober" # Boot
pacman -S "vim" "zsh" # Utilities
pacman -S "gnome" "gnome-tweaks" "xdg-desktop-portal-gnome" # for gnome
pacman -S "sway" "swaylock" "swayidle" "dmenu" "alacritty" "xdg-desktop-portal-wlr" "networkmanager" "bluez" # for sway
```

## Grub

```shell
# Install grub
mount "/dev/sdx1" "/boot"
grub-install --target="x86_64-efi" --efi-directory="/boot" --bootloader-id="GRUB"

# Generate config
# add "GRUB_DISABLE_OS_PROBER=false" to /etc/default/grub in order to detect other OSs
grub-mkconfig -o "/boot/grub/grub.cfg"
```

## Enable Services

```shell
# Enable services
systemctl enable "gdm.service" # for gnome only
systemctl enable "NetworkManager.service"
systemctl enable "bluetooth.service"
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
