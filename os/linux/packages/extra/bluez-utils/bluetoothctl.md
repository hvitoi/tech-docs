# bluetoothctl

## list

```shell
# List controllers
bluetoothctl list
```

## device

```shell
# List available devices
bluetoothctl devices # all
bluetoothctl devices Paired
bluetoothctl devices Bonded
bluetoothctl devices Trusted
bluetoothctl devices Connected

# Show info about a device (from /var/lib/bluetooth/<controller-id>/<device-id>/info)
bluetoothctl info "mac-addr"
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

## LinkKey

- LinkKey is an unique id created at the device pairing
- Stored at `/var/lib/bluetooth/<controller-id>/<device-id>/info`
- In order to pair device across OS's in the same machine, you must use the same key for both OS's
- You can get the LinkKey on windows with `chntpw` and on macos with `Keychain Access`
  - `Local Items` -> `Search Bluetooth` -> `Get MobileBluetooth devices`

## IdentityResolvingKey / PeripheralLongTermKey / SlaveLongTermKey

- For Bluetooth Low Energy (LE) devices, these 3 keys are set up on the connection
- To pair simultaneous with MacOS, get the get these keys in `Keychain Access` (search bluetooth)
  - `Local Items` -> `Search Bluetooth` -> `Get UUID devices`
- Keys
  - `Long-term Key` -> `PeripheralLongTermKey` and `SlaveLongTermKey`
  - `Remote IRK` -> `IdentityResolvingKey`
- The keys in MacOS must be decoded from base64 into hex

```shell
echo -n "mykeybase64" | base64 -d | od -t x1 -An | tr -d ' ' | tr "[a-z]" "[A-Z]"
```

## Connecting

```shell
service bluetooth start
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
