# cpupower

- `intel_pstate` is the CPU power scaling driver used for modern intel CPUs
- Config is saved at `/etc/default/cpupower`

## frequency-info

```shell
cpupower frequency-info
```

## frequency-set

```shell
# set maximum clock
cpupower frequency-set -u "3.0GHz"

# set minimum clock
cpupower frequency-set -d "800MHz"

# fixed clock frequency
cpupower frequency-set -f "2.0GHz"

# clock frequency based on a scaling governor
cpupower frequency-set -g "powersave"
cpupower frequency-set -g "performance"
```

## Configuration

```conf
# /etc/default/cpupower
max_freq='2.8GHz'
```

## /proc/cpuinfo

```shell
# Clock frequency
watch -n.5 "grep \"^[c]pu MHz\" /proc/cpuinfo"
watch "cat /sys/devices/system/cpu/cpu[0-9]*/cpufreq/scaling_cur_freq"
```

```shell
# Get scaling governor
cat "/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"

# Set scaling governor
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
echo powersave | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```
