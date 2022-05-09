# nmcli

- First the service must be enabled `systemctl enable NetworkManager.service`
- `nm-connection-editor` to open GUI

```shell
# general connection status
nmcli
```

## device

```shell
# Show all devices and its status
nmcli device status # or nmcli device

# Show specific device
nmcli device show "wlp3s0"

# Show wifi networks
nmcli device wifi list

# Connect to wifi
nmcli device wifi connect "SSID_or_BSSID" password "password"

# Show password of current wifi
nmcli device wifi show-password
```

## connection

```shell
# Show all connections (wifi, bridge, vpn, ethernet)
nmcli connection
nmcli connection show

# Up a connection
nmcli connection up "connection-name"
```
