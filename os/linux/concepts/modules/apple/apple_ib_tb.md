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