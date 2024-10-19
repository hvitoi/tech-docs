# AWS::SecretsManager::Secret

- Store `secrets`
- Alternative to SSM
- Enforces `rotation` every N days
- `Encrypted` using KMS
- Mostly meant for `RDS`

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html>

```yaml
Type: AWS::SecretsManager::Secret
Properties:
  Description: String
  GenerateSecretString:
    GenerateSecretString
  KmsKeyId: String
  Name: String
  ReplicaRegions:
    - ReplicaRegion
  SecretString:
    String
  Tags:
    - Tag
```
