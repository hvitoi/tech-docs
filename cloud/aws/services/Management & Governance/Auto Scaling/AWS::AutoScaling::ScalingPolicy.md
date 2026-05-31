# AWS::AutoScaling::ScalingPolicy

- **Scale based on SQS queue length**
  - Scale horizontally the consumers
  - Scaling the ASG can be based on the custom metric `Queue Length` (from CloudWatch)
    ![SQS with ASG](.images/sqs-asg.png)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html>

### PolicyType

- **TargetTrackingScaling**
  - Based on a metric
  - SQS queue
  - E.g., CPUUtilization, RequestCountPerTarget, Average Network In / Out
- **StepScaling**
  - Based on alarm from `CloudWatch`
- **Simple Scaling** (default)
  - Based on alarm from `CloudWatch`
- **PredictiveScaling**
  - Continuously forecast load and schedule scaling ahead

If multiple policies are reached at the same time, the one that scales more instances is triggered
