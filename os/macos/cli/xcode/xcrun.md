# xcrun

```shell
# list apple devices
xcrun simctl list "devices" "booted"

# launch by device name
xcrun simctl boot "iPhone 12"

# create
xcrun simctl create 'iPhone 11 14.4' \
  "com.apple.CoreSimulator.SimDeviceType.iPhone-11" \
  "com.apple.CoreSimulator.SimRuntime.iOS-14-4"
```
