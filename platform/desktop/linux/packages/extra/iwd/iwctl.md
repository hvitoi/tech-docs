# iwctl

- It's an alternative to `wpa_supplicant`
- In general `iwd` is more modern, easy to use and well maintained

## device

```shell
iwctl
[iwd] device list
```

## station

```shell
iwctl
[iwd] station "wlan0" get-networks
[iwd] station "wlan0" connect "ssid"
```
