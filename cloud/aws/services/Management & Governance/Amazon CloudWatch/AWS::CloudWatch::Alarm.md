# AWS::CloudWatch::Alarm

- Alarm triggering based on a metric
- Use the command `aws cloudwatch put-metric-alarm` to create it

## Alarm states

- `OK`
- `INSUFFICIENT_DATA`
- `ALARM`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html>

### AlarmActions

- `Notification` (SNS)
- `Lambda action`
- `Auto Scaling action`
- `EC2 action`
- `Systems Manager action`
- `Investigation action`

### Period

- Time range to analyze
