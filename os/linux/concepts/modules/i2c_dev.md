# i2c-dev

- `i2c-dev` is the module to control external monitor brightness over I2C
- <https://www.reddit.com/r/kde/comments/epgs13/kde_my_journey_to_get_a_brighness_slider_for_my/>

```shell
modprobe i2c_dev # Manual one-time load
```

```conf
# /etc/modules-load.d/i2c_dev.conf
i2c_dev
```

- **ddcutil** packages contains a tools to manage the capabilities
- **i2c-tools** is necessary for a good integration with the module. Rememver to set the correct permissions
