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
- Info
  - **LinkKey**: conventional bluetooth devices
  - **IdentityResolvingKey** (Remote IRK): BLE
  - **PeripheralLongTermKey** (Long-term Key): BLE
  - **SlaveLongTermKey** (Long-term Key): BLE

### Windows

- Get the keys with `chntpw`

## MacOS

- Access `Keychain access`
- Search for "bluetooth"
- Conventional bluetooth devices will show up as `MobileBluetooth`, bluetooth BLE devices will show up as an `UUID`

```shell
# Decode keys from base64 into hex
echo -n "mykeybase64" | base64 -d | od -t x1 -An | tr -d ' ' | tr "[a-z]" "[A-Z]"
```

## Connecting

```shell
btmgmt power off
btmgmt privacy on
btmgmt power on
bluetoothctl
> scan on
(turn on the device and enter pairing mode, wait for it to be detected)
> scan off
> pair <address>
> connect <address>
> trust <address>
(power-cycle the device)
[agent] Accept pairing (yes/no): yes
```
