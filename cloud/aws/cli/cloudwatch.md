# aws cloudwatch

## Metrics

### list-metrics

```shell
aws cloudwatch list-metrics --namespace fis
aws cloudwatch list-metrics --namespace AWS/EC2 --metric-name "StatusCheckFailed_Instance"
```

### put-metric-data

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

## Alarms

### put-metric-alarm

- Create an alarm
- The alarm is created based on a metric

```shell
# Based on EKS metrics
aws cloudwatch put-metric-alarm \
  --alarm-name 'MyAlarm' \
  --metric-name 'node_cpu_utilization' \
  --namespace 'ContainerInsights' \
  --statistic 'Average' \
  --dimensions '[{"Name":"ClusterName","Value":"my-cluster"}]' \
  --period 60 \
  --evaluation-periods 1 \
  --datapoints-to-alarm 1 \
  --threshold 30 \
  --comparison-operator 'GreaterThanThreshold' \
  --actions-enabled \
  --treat-missing-data 'missing'

# Based on EC2 metrics
aws cloudwatch put-metric-alarm \
  --alarm-name "MyAlarm" \
  --alarm-description "Alarm when CPU exceeds 80% for 5 minutes" \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --period 300 \
  --evaluation-periods 1 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --alarm-actions arn:aws:sns:us-east-1:123456789012:MyTopic \
  --unit Percent
```

### set-alarm-state

```shell
# Trigger alarm
aws cloudwatch set-alarm-state \
  --alarm-name "myalarm" \
  --state-value "ALARM" \
  --state-reason "testing"
```
