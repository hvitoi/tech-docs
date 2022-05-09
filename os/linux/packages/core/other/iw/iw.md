# iw

- Network manager using `ip` command

## list

- Get device capabilities for all devices
- Such as band information (2.4 GHz, and 5 GHz), and 802.11n information

```shell
iw list
```

## event

- Listening to events

```shell
iw event
```

## phy (directory)

- Add a new interface
  - `monitor`
  - `managed` [also station]
  - `wds`
  - `mesh` [also mp]
  - `ibss` [also adhoc]

```shell
iw phy "phy0" interface add "mynewinterface" type "monitor"
iw phy "phy0" interface add "mynewinterface" type "managed" # ...
```

## dev (device)

```shell
# Show all interfaces information
iw dev
```

### link

```shell
# link status
iw dev "wlp3s0" link
```

### info

```shell
# Show specific interface information
iw dev "wlp3s0" info # type "managed" means it only accepts packages directed to this mac address
```

### scan

```shell
# Scan wi-fi in an interface
iw dev "wlp3s0" scan | less
```

### connect

```shell
# Connect to a network in an interface
iw dev "wlp3s0" connect "ssid"
```

### set

- Set a property of an interface
- The interface must be disabled first (`ip link set wlp3s0 down/up`)

```shell
iw dev "wlp3s0" set monitor control # monitor mode
iw dev "wlp3s0" set type managed # managed mode
```

### del

```shell
# delete interface
iw dev "interface-name" del
```
