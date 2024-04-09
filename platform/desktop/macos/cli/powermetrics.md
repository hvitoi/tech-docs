# powermetrics

```shell
# MacbookPro16 very high CPU temperature ~90 C
powermetrics --samplers smc | grep -i "CPU die temperature"
powermetrics --samplers smc | grep -i "GPU die temperature"
powermetrics --samplers smc | grep -i "Fan" # MacbookPro16 max fan speed ~5400 rpm

# All sensors
powermetrics --samplers smc -i1 -n1
```
