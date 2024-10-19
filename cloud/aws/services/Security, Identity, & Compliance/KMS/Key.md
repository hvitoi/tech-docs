# AWS::KMS::Key

- Store and manage `encryption keys`
- Integrates with all aws resources
- Audit key usage with CloudTrail
- Pay per API call

## Key Types

- `Symmetric` (AES-256): always access the key via KMS API (never unencrypted)
- `Asymmetric` (RSA & ECC): can be accessed directly

## Key Origin

- `AWS Managed Key`: free (starts with prefix "aws/". E.g., "aws/s3)
- `Customer Managed Keys created`: $1/month (created or imported)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html>

```yaml
Type: AWS::KMS::Key
Properties:
  BypassPolicyLockoutSafetyCheck: Boolean
  Description: String
  Enabled: Boolean
  EnableKeyRotation: Boolean
  KeyPolicy: Json
  KeySpec: String
  KeyUsage: String
  MultiRegion: Boolean
  Origin: String
  PendingWindowInDays: Integer
  RotationPeriodInDays: Integer
  Tags:
    - Tag
```

### EnableKeyRotation

- KMS can `rotate` the keys
- Only for `Customer-managed CMK`
- Every year a new key is created automatically with the same `CMK ID`
- Old keys are kept to access old data

- With `manual rotation`, the new key has different CMK ID
- WIth manual rotation, it's good to use the same `alias` for the new keys

### KeyPolicy

- Cannot control access without it!
- `Default Key Policy`
  - Allow all users and roles (root user) access to the KMS key
- `Custom Key Policy`
  - Define users and roles for _use_
  - Define users and roles for _administration_
  - Useful for cross-account access

### PendingWindowInDays

- Keys deleted remain in `pending` state for some time before being permanently deleted
- Specifies the `number of days` (7 - 30 days) in the waiting period before AWS KMS deletes a KMS key that has been removed
