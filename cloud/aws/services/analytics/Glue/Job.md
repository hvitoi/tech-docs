# AWS::Glue::Job

- Managed serverless `Extract, Transform, and Load` (ETL) service
- Extracts data from `s3`, `rds` and others
- Useful to prepare and transform for analytics

![Glue](.images/glue.png)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html>

```yaml
Type: AWS::Glue::Job
Properties:
  AllocatedCapacity: Number
  Command:
    JobCommand
  Connections:
    ConnectionsList
  DefaultArguments: Json
  Description: String
  ExecutionClass: String
  ExecutionProperty:
    ExecutionProperty
  GlueVersion: String
  JobMode: String
  JobRunQueuingEnabled: Boolean
  LogUri: String
  MaintenanceWindow: String
  MaxCapacity: Number
  MaxRetries: Number
  Name: String
  NonOverridableArguments: Json
  NotificationProperty:
    NotificationProperty
  NumberOfWorkers: Integer
  Role: String
  SecurityConfiguration: String
  Tags:
    - Tag
  Timeout: Integer
  WorkerType: String
```
