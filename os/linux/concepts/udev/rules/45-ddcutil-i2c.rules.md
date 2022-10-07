# 45-ddcutil-i2c.rules

- Rules for allowing access to `i2c` devices (displays)
- Used by `ddcutil` usually to access the display capabilities

```conf
# On some distributions, package i2c-tools provides a udev rule.
# For example, on Ubuntu, see 40-i2c-tools.rules.

# Assigns the i2c devices to group i2c, and gives that group RW access:
KERNEL=="i2c-[0-9]*", GROUP="i2c", MODE="0660"

# Gives everyone RW access to the /dev/i2c devices:
# KERNEL=="i2c-[0-9]*",  MODE="0666"
```
