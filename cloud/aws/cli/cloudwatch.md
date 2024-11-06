# aws cloudwatch

## list-metrics

```shell
aws cloudwatch list-metrics --namespace fis
aws cloudwatch list-metrics --namespace AWS/EC2 --metric-name "StatusCheckFailed_Instance"
```

## put-metric-data

```shell
# custom metric
aws cloudwatch put-metric-data \
  --namespace "Usage Metrics" \
  --metric-data "file://metric.json"

aws cloudwatch put-metric-data \
  --namespace "Usage Metrics" \
  --metric-name "Buffers" \
  --unit "Bytes" \
  --value "23147294" \
  --dimensions "InstanceId=1-12344,InstanceType=m1.small"
```

## set-alarm-state

```shell
# Trigger alarm
aws cloudwatch set-alarm-state \
  --alarm-name "myalarm" \
  --state-value "ALARM" \
  --state-reason "testing"
```
