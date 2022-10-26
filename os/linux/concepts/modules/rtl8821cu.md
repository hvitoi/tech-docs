# rtl8821cu

- Wifi dongle firmware
- Get the dkms from `rtl8821cu-morrownr-dkms-git` (aur)
- You might need to change the dongle usb mode from cd-rom to pci device

```sh
# try
eject /dev/sr0

# if not, try
usb_modeswitch -KW -v 0bda -p 1a2b
```
