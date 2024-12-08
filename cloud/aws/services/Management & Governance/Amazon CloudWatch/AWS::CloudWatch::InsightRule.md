# AWS::CloudWatch::InsightRule

- Provide `metrics` for every service in AWS
- Cloudwatch is commonly used as base for `auto scaling`
- `Source`: Elastic Beanstalk, EC2, VPC, SDK, ...
- `Sink`: S3, ElasticSearch, ...

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html>

```yaml
Type: AWS::CloudWatch::InsightRule
Properties:
  RuleBody: String
  RuleName: String
  RuleState: String
  Tags:
    - Tag
```

### RuleBody

- Define and send your own custom metrics to CloudWatch
- Use API `PutMetricData` to send values
- `MetricResolution`: _Standard_ (1min), _High Resolution_ (10 or 30 seconds)

```shell
aws cloudwatch put-metric-data \
  --namespace "Usage Metrics" \
  --metric-data "file://metric.json"
```
