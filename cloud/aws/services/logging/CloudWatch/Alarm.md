# AWS::CloudWatch::Alarm

- Alarm triggering based on a metric
- Alarm states: `OK`, `INSUFFICIENT_DATA`, `ALARM`
- Period: timerange to analyze

- `Actions`: EC2, auto scaling, SNS

```sh
aws cloudwatch set-alarm-state \
  --alarm-name "myalarm" \
  --state-value "ALARM" \
  --state-reason "testing"
```
