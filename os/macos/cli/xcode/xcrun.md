# xcrun

## simctl

- CLI to control the iOS simulator

## list

- Lists:
  - `devices`
  - `device types`
  - `runtimes`
  - `device pairs`

```shell
xcrun simctl list devices
xcrun simctl list devicetypes
xcrun simctl list runtimes
xcrun simctl list pairs
```

## create

- Create a device
- If runtime is not specified, use the latest

```shell
xcrun simctl create "<device-name>" "<device type id>" "[<runtime id>]"

# Create
xcrun simctl create 'My iPhone 14 Pro Max' \
  "com.apple.CoreSimulator.SimDeviceType.iPhone-14-Pro-Max"
```

### boot

- Boot a device or device pair
- The device must be created before hand

```shell
xcrun simctl boot "<device-name>"
```
