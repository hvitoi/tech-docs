# v4l2loopback-dkms

- DKMS package: **v4l2loopback-dkms**

```shell
# Load loopback device temporarely
modprobe v4l2loopback exclusive_caps=1 max_buffers=2
lsmod | grep v4l2loopback
```

```conf
# /etc/modules-load.d/v4l2loopback.conf
v4l2loopback
```

```conf
# /etc/modprobe.d/v4l2loopback.conf
options v4l2loopback exclusive_caps=1
options v4l2loopback max_buffers=2
options v4l2loopback width=1920
options v4l2loopback height=1080
```
