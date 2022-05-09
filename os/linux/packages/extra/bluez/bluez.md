# bluez

## Fix buzz sound when idle

- Disable hibernation for this hardware at `snd_hda_intel` module
- `/etc/modprobe.d/modprobe.conf`

```conf
# Add this line
options snd_hda_intel power_save=0
options snd_hda_intel power_save_controller=N # optional
```

## Bluetooth random disconnect

- Disable autosuspend for btusb
- `/etc/modprobe.d/btusb.conf`

```conf
options btusb enable_autosuspend=n
```
