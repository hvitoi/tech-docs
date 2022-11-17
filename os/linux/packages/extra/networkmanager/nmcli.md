# nmcli

- First the service must be enabled `systemctl enable NetworkManager.service`
- `nm-connection-editor` to open GUI

```sh
# general connection status
nmcli
```

## device

```sh
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

```sh
# Show all connections (wifi, bridge, vpn, ethernet)
nmcli connection
```

```sh
# import a connection configuration
nmcli connection import \
  type "wireguard" \
  file "wg0.conf"
```

```sh
nmcli connection show "wg0"
```

```sh
# Up a connection
nmcli connection up "connection-name"
```

```sh
nncli connection modify "wg0" \
  connection.autoconnect "no"

nncli connection modify "wg0" \
  connection.id "Awesome_vpn"

nncli connection modify "wg0" \
  connection.interface-name "wg1"
```

```sh
nmcli connection delete "wg0"
```
