# caffeinate

- Prevents the system from turning off

```shell
# prevent the system from idle sleeping
caffeinate
caffeinate -i # same

# prevent the system from idle sleeping (only when connected to power)
caffeinate -s

# prevent the disk from idle sleeping
caffeinate -m

# system idle sleep (when running on AC only)
caffeinate -s
```
