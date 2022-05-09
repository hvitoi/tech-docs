# grub-mkconfig

```shell
# Generate grub config from /etc/default/grub
grub-mkconfig -o "/boot/grub/grub.cfg"
```

## Kernel Parameters

- Check the parameters your system was booted up with at `/proc/cmdline`

### Temporary parameters

- Press `e` when the menu shows up and add them on the linux line

```txt
linux /boot/vmlinuz-linux root=UUID=0a3407de-014b-458b-b5c1-848e92a327a3 rw loglevel=3 quiet splash video=1920x1080
```

- Press `ctrl + x` to boot with these parameters.

### Permanent parameters

- To make the change persistent after reboot, edit `/etc/default/grub` and append your kernel options between the quotes in the `GRUB_CMDLINE_LINUX_DEFAULT` line

```conf
GRUB_DEFAULT="0" # index to boot (from the entry list in /boot/grub/grub.cfg)
GRUB_TIMEOUT="2" # timeout in seconds
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash" # kernel parameters
GRUB_DISABLE_OS_PROBER=false # detect other OS's
```

- And then re-generate the `grub.cfg`
