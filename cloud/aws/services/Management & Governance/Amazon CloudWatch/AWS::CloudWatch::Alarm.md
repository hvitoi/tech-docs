# AWS::CloudWatch::Alarm

- Alarm triggering based on a metric
- Use the command `aws cloudwatch put-metric-alarm` to create it

## Alarm states

- `OK`
- `INSUFFICIENT_DATA`
- `ALARM`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html>

```yaml
Type: AWS::CloudWatch::Alarm
Properties:
  ActionsEnabled: Boolean
  AlarmActions:
    - String
  AlarmDescription: String
  AlarmName: String
  ComparisonOperator: String
  DatapointsToAlarm: Integer
  Dimensions:
    - Dimension
  EvaluateLowSampleCountPercentile: String
  EvaluationPeriods: Integer
  ExtendedStatistic: String
  InsufficientDataActions:
    - String
  MetricName: String
  Metrics:
    - MetricDataQuery
  Namespace: String
  OKActions:
    - String
  Period: Integer
  Statistic: String
  Tags:
    - Tag
  Threshold: Number
  ThresholdMetricId: String
  TreatMissingData: String
  Unit: String
```

### AlarmActions

- `Notification` (SNS)
- `Lambda action`
- `Auto Scaling action`
- `EC2 action`
- `Systems Manager action`
- `Investigation action`

### Period

- Time range to analyze
