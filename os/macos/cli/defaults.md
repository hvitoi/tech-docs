# defaults

```shell
# read all config
defaults read

# read any config
defaults read <domain> <key>
defaults read "com.apple.bluetoothd.plist" "LinkKeys"

# key press configurations
defaults write -g InitialKeyRepeat -int 10 # normal minimum is 15 (225 ms)
defaults write -g KeyRepeat -int 1 # normal minimum is 2 (30 ms)
```
