# AWS::SES::EmailIdentity

- Before sending emails on one's behalf, you need first verify the address by creating an `Email Identity`
- The verification is only necessary for using the given email as the sender

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html>

```yaml
Type: AWS::SES::EmailIdentity
Properties:
  ConfigurationSetAttributes:
    ConfigurationSetAttributes
  DkimAttributes:
    DkimAttributes
  DkimSigningAttributes:
    DkimSigningAttributes
  EmailIdentity: String
  FeedbackAttributes:
    FeedbackAttributes
  MailFromAttributes:
    MailFromAttributes
```
