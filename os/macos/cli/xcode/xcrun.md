# xcrun

```shell
# list apple devices
xcrun simctl list devices

# launch by device name
xcrun simctl boot "iPhone 12"

# create (specifying device-type and runtime)
xcrun simctl create 'iPhone 11 14.4' \
  "com.apple.CoreSimulator.SimDeviceType.iPhone-11" \
  "com.apple.CoreSimulator.SimRuntime.iOS-14-4"

# create (specifying device-type and latest runtime)
xcrun simctl create 'iPhone 14 Pro Max' \
  "com.apple.CoreSimulator.SimDeviceType.iPhone-14-Pro-Max"
```
