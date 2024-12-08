# AWS::KMS::ReplicaKey

- KMS keys are bound to a region
- In order to copy resource `snapshots` to another regions, a new KMS key in the new region must be set
- The new key must also have the correct policies

![KMS snapshots](.images/kms-snapshots.png)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-replicakey.html>

```yaml
Type: AWS::KMS::ReplicaKey
Properties:
  Description: String
  Enabled: Boolean
  KeyPolicy: Json
  PendingWindowInDays: Integer
  PrimaryKeyArn: String
  Tags:
    - Tag
```
