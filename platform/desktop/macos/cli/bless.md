# bless

```shell
# Make a new snapshot and tell the system trust this non-SSV authenticated system
bless \
  --folder /[mountpath]/System/Library/CoreServices \
  --bootefi \
  --create-snapshot

# set a system volume as default boot volume
bless
  --setBoot \
  --device /dev/disk0s0 \
  --user <admin_user>
```
