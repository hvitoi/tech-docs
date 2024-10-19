# AWS::KinesisAnalyticsV2::Application

- Similar to `kSQL`
- Analyze data streams with `SQL` or `Flink`
- Use cases
  - Time-series analytics
  - Real-time dashboards
  - Real-time metrics

![Data Analytics](.images/kinesis-data-analytics.png)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html>

```yaml
Type: AWS::KinesisAnalyticsV2::Application
Properties:
  ApplicationConfiguration:
    ApplicationConfiguration
  ApplicationDescription: String
  ApplicationMaintenanceConfiguration:
    ApplicationMaintenanceConfiguration
  ApplicationMode: String
  ApplicationName: String
  RunConfiguration:
    RunConfiguration
  RuntimeEnvironment: String
  ServiceExecutionRole: String
  Tags:
    - Tag
```
