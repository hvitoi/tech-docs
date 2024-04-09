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

## i2c-tools

- `i2c-tools` package is installed as a dependency for a good integration with `i2c_dev` module

```shell
pacman -S "i2c-tools"
groupadd --system "i2c" # create i2c group (if not exists already)
cp "/usr/share/ddcutil/data/45-ddcutils-i2c.rules" "/etc/udev/rules.d" # Copy the udev rule for the new group to rules.d
usermod -aG "i2c" "hvitoi"  # add user to the i2c group
```
