# nmcli

- First the service must be enabled `systemctl enable NetworkManager.service`
- `nm-connection-editor` to open GUI

```shell
# general connection status
nmcli
```

## device

- Devices
  - wlp5s0
  - wg0
  - lo
  - etc

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

- Connection
  - MyWifiHome
  - Mullvad
  - lo (Loopback)
  - etc

```shell
# Show all connections (wifi, bridge, vpn, ethernet)
nmcli connection
```

```shell
# import a connection configuration
nmcli connection import \
  type "wireguard" \
  file "wg0.conf"
```

```shell
nmcli connection show "wg0"
```

```shell
# Up a connection
nmcli connection up "connection-name"
```

```shell
nncli connection modify "wg0" \
  connection.autoconnect "no"

nncli connection modify "wg0" \
  connection.id "Awesome_vpn"

nncli connection modify "wg0" \
  connection.interface-name "wg1"
```

```shell
nmcli connection delete "wg0"
```
