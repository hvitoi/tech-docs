# 61-mutter-primary-gpu.rules

- Responsible for deciding which GPU to use as primary

```conf
ENV{DEVNAME}=="/dev/dri/card1", TAG+="mutter-device-preferred-primary"
```
