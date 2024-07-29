# AWS::CloudWatch::MetricStream

- Metrics streams can automatically stream CloudWatch metrics to AWS destinations including Amazon S3

```yaml
Type: AWS::CloudWatch::MetricStream
Properties:
  ExcludeFilters:
    - MetricStreamFilter
  FirehoseArn: String
  IncludeFilters:
    - MetricStreamFilter
  Name: String
  OutputFormat: String
  RoleArn: String
  Tags:
    - Tag
```
