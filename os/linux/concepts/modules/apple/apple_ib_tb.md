# apple_ib_tb

- Touchbar settings

## Configuration

```conf
# /etc/modprobe.d/apple-ib-tb.conf

# 0: Only show F1-F12
# 1: Show media and brightness controls, use the fn key to switch to F1-F12
# 2: Show F1-F12, use the fn key to switch to media and brightness controls
# 3: Only show media and brightness controls
# 4: Only show the escape key
options apple_ib_tb fnmode=1
```

## Issues with suspend

- This module causes trouble when system is suspended
- Ideally it should be disabled before the system is suspended

```bash
# rmmod_tb.sh

#!/usr/bin/env bash
if [ "${1}" = "pre" ]; then
        modprobe -r apple_ib_tb
elif [ "${1}" = "post" ]; then
        modprobe apple_ib_tb
fi
```

```shell
# copy the script into the sleep hooks
cp "./rmmod_tb.sh" "/lib/systemd/system-sleep/rmmod_tb.sh"

# change permissions
chmod 755 "/lib/systemd/system-sleep/rmmod_tb.sh"
chown root:root "/lib/systemd/system-sleep/rmmod_tb.sh"
```
