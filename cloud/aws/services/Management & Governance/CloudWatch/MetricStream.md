# AWS::CloudWatch::MetricStream

- Metrics streams can automatically stream CloudWatch metrics to AWS destinations including Amazon S3

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html>

```yaml
Type: AWS::CloudWatch::MetricStream
Properties:
  ExcludeFilters:
    - MetricStreamFilter
  FirehoseArn: String
  IncludeFilters:
    - MetricStreamFilter
  IncludeLinkedAccountsMetrics: Boolean
  Name: String
  OutputFormat: String
  RoleArn: String
  StatisticsConfigurations:
    - MetricStreamStatisticsConfiguration
  Tags:
    - Tag
```
