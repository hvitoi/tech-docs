# powermetrics

```sh
# MacbookPro16 very high CPU temperature ~90 C
powermetrics --samplers smc | grep -i "CPU die temperature"

# MacbookPro16 max fan speed ~5400 rpm
powermetrics --samplers smc | grep Fan
```
