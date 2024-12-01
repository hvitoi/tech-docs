# AWS::IAM::VirtualMFADevice

- Enables `MFA` (Multi Factor Authentication)
- MFA for the root user is activated under `My Security Credentials` at the account upper tab
- MFA for IAM users is activated under `My Security Credentials` at user in IAM

## Properties

- <https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/aws-resource-iam-virtualmfadevice.html>

```yaml
Type: AWS::IAM::VirtualMFADevice
Properties:
  Path: String
  Tags:
    - Tag
  Users:
    - String
  VirtualMfaDeviceName: String
```

### VirtualMfaDeviceName

- `Virtual MFA device` (google authenticator app, authy web app, etc)
- `Universal 2nd Factor (U2F) security key` (YubiKey physical device)
- `Hardware MFA Device` (Gemalto Key Fob)
