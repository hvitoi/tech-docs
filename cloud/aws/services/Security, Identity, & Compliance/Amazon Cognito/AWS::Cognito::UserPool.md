# AWS::Cognito::UserPool

- `Cognito User Pools` (CUP)

- `Database of users` for mobile apps
- You can either provide `built-in user management` or integrate with `external identity providers` (fb, google, etc)

- Gets a JWT as return

- Can be integrated with API Gateway for authentication
- Integrate with Facebook to provide authenticated logins for your application users.

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html>

```yaml
Type: AWS::Cognito::UserPool
Properties:
  AccountRecoverySetting:
    AccountRecoverySetting
  AdminCreateUserConfig:
    AdminCreateUserConfig
  AliasAttributes:
    - String
  AutoVerifiedAttributes:
    - String
  DeletionProtection: String
  DeviceConfiguration:
    DeviceConfiguration
  EmailAuthenticationMessage: String
  EmailAuthenticationSubject: String
  EmailConfiguration:
    EmailConfiguration
  EmailVerificationMessage: String
  EmailVerificationSubject: String
  EnabledMfas:
    - String
  LambdaConfig:
    LambdaConfig
  MfaConfiguration: String
  Policies:
    Policies
  Schema:
    - SchemaAttribute
  SmsAuthenticationMessage: String
  SmsConfiguration:
    SmsConfiguration
  SmsVerificationMessage: String
  UserAttributeUpdateSettings:
    UserAttributeUpdateSettings
  UsernameAttributes:
    - String
  UsernameConfiguration:
    UsernameConfiguration
  UserPoolAddOns:
    UserPoolAddOns
  UserPoolName: String
  UserPoolTags:
    Key: Value
  VerificationMessageTemplate:
    VerificationMessageTemplate
```

### EmailConfiguration

- Support for email verifying

### MfaConfiguration

- Support for MFA
