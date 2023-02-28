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
```

## /proc/cpuinfo

```shell
# Monitor clock frequency
watch -n.5 "grep \"^[c]pu MHz\" /proc/cpuinfo"
watch "cat /sys/devices/system/cpu/cpu[0-9]*/cpufreq/scaling_cur_freq"
```
