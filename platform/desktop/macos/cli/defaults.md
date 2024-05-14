# defaults

```shell
# read all config
defaults read

# read
defaults read <domain> <key>
defaults read "com.apple.bluetoothd.plist" "LinkKeys"

# write
defaults write -g InitialKeyRepeat -int 10 # normal minimum is 15 (225 ms)
defaults write -g KeyRepeat -int 1 # normal minimum is 2 (30 ms)

# delete
defaults delete /Library/Preferences/com.apple.DiskArbitration.plist IgnoredDiskUUIDs
```
