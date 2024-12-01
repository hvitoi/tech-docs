# AWS::Organizations::Account

- An account alias can be created in order to access the account (with any IAM user) from custom URI. <https://hvitoi.signin.aws.amazon.com/console>
- Access to Billing Information is not granted, even with administrator policy. For that, special config must be set up
- `Password policies` can be set for all users under `Account Settings`

```yaml
Type: AWS::Organizations::Account
Properties:
  AccountName: String
  Email: String
  ParentIds:
    - String
  RoleName: String
  Tags:
    - Tag
```
