# 61-mutter-primary-gpu.rules

- Responsible for deciding which GPU to use as primary

```conf
ENV{DEVNAME}=="/dev/dri/card1", TAG+="mutter-device-preferred-primary"
ENV{DEVNAME}=="/dev/dri/by-path/pci-0000:0e:00.0-card", TAG+="mutter-device-preferred-primary"
```
