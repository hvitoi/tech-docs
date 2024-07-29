# AWS::Logs::LogGroup

- A log group defines common `properties` for `log streams`
- Each log stream must belong to one log group

```yaml
Type: AWS::Logs::LogGroup
Properties:
  KmsKeyId: String
  LogGroupName: String
  RetentionInDays: Integer
```

## RetentionInDays

- `Expiration Policy`: 30 days, etc
