# grub-install

```shell
# Preparation
pacman -S "grub" "efibootmgr" "os-prober"
mount "/dev/sdx1" "/boot"

# Install
grub-install \
  --target="x86_64-efi" \
  --efi-directory="/boot" \
  --bootloader-id="GRUB"

# Generate config file
grub-mkconfig -o "/boot/grub/grub.cfg"
```

```shell
# Non-arch
sudo mount "/dev/sdx1" "/mnt"
for i in /dev /dev/pts /proc /sys /run; do
  sudo mount -B $i /mnt$i
done
sudo chroot /mnt

mount "/dev/sda1" "/boot"
grub-install "/dev/sda"
update-grub
```
