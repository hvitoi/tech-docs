# AWS::Organizations::Account

- Access to Billing Information is not granted, even with administrator policy. For that, special config must be set up
- `Password policies` can be set for all users under `Account Settings`
- ARN example: `arn:aws:organizations::123456789012:account/o-abcdccusvz/123403787789`

## Management account (master account)

- An organization always have a `management account` (formerly known as "master account")
- You can't remove a `management account` from an organization
- If you want the management account to become a member account in another organization, you must first delete the current organization of the management account.

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html>

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
