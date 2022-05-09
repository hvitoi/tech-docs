# ddcutil

- It's a backlight utility package that can be used to query and set brightness settings

```shell
ddcutil capabilities # "Feature: 10" is brightness
ddcutil environment
ddcutil detect

# Brightness
ddcutil getvcp 10 # Get current brightness value
ddcutil setvcp 10 70 # Set brightness to 70
ddcutil setvcp 10 + 10 # -10 brightness

```

- `Brightness control using ddcutil` gnome extension to control external monitor brightness
- <https://extensions.gnome.org/extension/2645/brightness-control-using-ddcutil/>
