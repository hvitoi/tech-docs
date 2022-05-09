# i2c-tools

- `i2c-tools` package must be installed for a good integration with `i2c-dev` module

```shell
pacman -S "i2c-tools"
groupadd --system "i2c" # create i2c group (if not exists already)
sudo cp "/usr/share/ddcutil/data/45-ddcutils-i2c.rules" "/etc/udev/rules.d" # Copy the udev rule for the new group to rules.d
usermod -aG "i2c" "hvitoi"  # add user to the i2c group
```
