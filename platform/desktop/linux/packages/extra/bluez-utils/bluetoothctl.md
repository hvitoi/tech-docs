# bluetoothctl

## list

- List controllers (usually one)

```shell
# List controllers
bluetoothctl list
```

## show

- Show controllers information

```shell
bluetoohctl show
```

## info

- Information about connected devices

```shell
bluetoothctl info

# Show info about a device (from /var/lib/bluetooth/<controller-id>/<device-id>/info)
bluetoothctl info "mac-addr"
```

## devices

```shell
# List available devices
bluetoothctl devices # all
bluetoothctl devices Paired
bluetoothctl devices Bonded
bluetoothctl devices Trusted
bluetoothctl devices Connected
```

## Pairing

```shell
# Scan devices
bluetoothctl scan on

# Pair
bluetoothctl pair "mac-addr"

# Cancel pairing process
bluetoothctl cancel-pairing "mac-addr"

# Unpair
bluetoothctl remove "mac-addr"
```

## Connection

```shell
# Connect
bluetoothctl connect "mac-addr"

# Disconnect
bluetoothctl disconnect "mac-addr"
```

## Trust

```shell
# Trust
bluetoothctl trust "mac-add"

# Untrust
bluetoothctl untrust "mac-add"
```

## Cross OS pairing

- Bluetooth info is stored at `/var/lib/bluetooth/<controller-id>/<device-id>/info`
- This bluetooth connection keys must be the same across the OS's

- _Conventional bluetooth devices_
  - **LinkKey**

- _BLE devices_
  - **IdentityResolvingKey** (Remote IRK)
  - **PeripheralLongTermKey** (Long-term Key)
  - **SlaveLongTermKey** (Long-term Key)

### Alongside MacOS

- Access `Keychain access`
- Search for "bluetooth"

- _Conventional bluetooth devices_
  - Show up as `MobileBluetooth`

- _BLE devices_
  - Show up as an `UUID`
  - These devices generate an increasing UUID on each pairing. In that case, get the exact UUID on MacOS and rename the folder on linux
  - Long-term Key and Remote IRK are base64 encoded, use the command below to convert it

```shell
# Decode keys from base64 into hex
echo -n "mykeybase64" | base64 -d | od -t x1 -An | tr -d ' ' | tr "[a-z]" "[A-Z]"
```

### Alongside Windows

- Get the keys with `chntpw`
