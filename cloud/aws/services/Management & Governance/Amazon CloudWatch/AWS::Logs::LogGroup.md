# AWS::Logs::LogGroup

- A log group defines common `properties` for `log streams`
- Each log stream must belong to one log group
- Log groups are created in `CloudWatch`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html>

```yaml
Type: AWS::Logs::LogGroup
Properties:
  DataProtectionPolicy: Json
  KmsKeyId: String
  LogGroupClass: String
  LogGroupName: String
  RetentionInDays: Integer
  Tags:
    - Tag
```

### RetentionInDays

- `Expiration Policy`: 30 days, etc
