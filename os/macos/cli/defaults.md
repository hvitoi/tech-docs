# defaults

```shell
# read all config
defaults read

# read any config
# for bluetooth linkkeys on macOS Monterey+, get it on Keychain Access
defaults read "com.apple.bluetoothd.plist" "LinkKeys"
```
