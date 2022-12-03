# bluetoothctl

## List

```shell
# List controllers
bluetoothctl list

# List available devices
bluetoothctl devices

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
- You can get the LinkKey on windows with `chntpw` and on macos with `key access`
