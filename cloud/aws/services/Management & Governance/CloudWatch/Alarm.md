# AWS::CloudWatch::Alarm

- Alarm triggering based on a metric
- Alarm states: `OK`, `INSUFFICIENT_DATA`, `ALARM`
- Period: timerange to analyze

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

- `Actions`: EC2, auto scaling, SNS
