# ddcci

- DKMS package: **ddcci-driver-linux-dkms**

- `DDC/CI` (Display Data Channel Command Interface) can be used to communicate with external monitors implementing `MCCS` (Monitor Control Command Set) over `I2C`
- Using `ddcci` and `i2c-dev` modules simultaneously may result in resource conflicts such as a Device or resource busy error
- DDC can control brightness, contrast, inputs, etc on supported monitors
- Expose external monitors in `sysfs` at `/sys/class/backlight/` (e.g., intel_backlight)
- Power level of backlight LEDs can be controlled using `ACPI` kernel module

```conf
# /etc/modules-load.d/ddcci.conf
ddcci
```

- Each detected DDC/CI device gets a directory in `/sys/bus/ddcci/devices`
- The main device on a bus is named `ddcci[I²C bus number]`
